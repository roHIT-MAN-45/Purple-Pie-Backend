from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Create User
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(payload : schemas.UserCreate, db: Session = Depends(get_db)):

    # Checking if user already exists or not
    user = db.query(models.User).filter(models.User.email == payload.email).first()

    if user:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail= f"User already exists")
   
    # Hashing password before storing it in database
    payload.password = utils.hash(payload.password)

    new_user = models.User(**payload.dict())
    db.add(new_user)
    db.commit()

    db.refresh(new_user)

    return new_user

# Get User by id
@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id : int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user: 
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"User with id: {id} does not exist")

    return user