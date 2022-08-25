from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from . import schemas, database, models
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'login')

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
EXPIRATION_TIME = settings.token_expiration_time

def generate_token(data : dict):
    # Copying data in another variable so we don't change it
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes = EXPIRATION_TIME)

    # Adding extra property to our data
    to_encode.update({"exp" : expire})

    # Generating token
    encoded_token = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)

    return encoded_token

# Verifies token data embeded in token
def verify_access_token(token : str, credentials_exception):
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id = id)

    except JWTError:
        raise credentials_exception

    return token_data

# Verifies the token is correct or not 
def get_current_user(token : str = Depends(oauth2_scheme), db: Session = Depends(database.get_db) ):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials", headers={"WWW-Authenticate" : "Bearer"})

    token_payload = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token_payload.id).first()
    
    return user