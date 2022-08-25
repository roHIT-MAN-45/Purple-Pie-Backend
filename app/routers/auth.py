from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, utils, oauth2

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model = schemas.Token)
def login_user(payload : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)) :

    # OAuth2PasswordRequestForm returns username instead of email in this case
    user = db.query(models.User).filter(models.User.email == payload.username).first()

    if not user : 
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = f"Invalid Credentials")

    if not utils.verify(payload.password, user.password):
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = f"Invalid Credentials")

    token = oauth2.generate_token(data = {"user_id" : user.id})

    return {"user_id" : user.id, "token" : token, "token_type" : "bearer"}