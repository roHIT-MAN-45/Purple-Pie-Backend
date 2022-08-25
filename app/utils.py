from passlib.context import CryptContext

# Running bcrypt algorithm to hash user password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

# Hashes the password
def hash(password: str):
    return pwd_context.hash(password)

# Verifies the password provided by user and hashed_password present in database
def verify(password, hashed_password):
    return pwd_context.verify(password, hashed_password)