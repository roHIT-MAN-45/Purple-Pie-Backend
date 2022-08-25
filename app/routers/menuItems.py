from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/menuitems",
    tags=["Menu Items"]
)

# Get Menu Items
@router.get('/', response_model=List[schemas.MenuItemResponse])
def getMenuItems(db: Session = Depends(get_db)):

    menu_items = db.query(models.MenuItem).all()

    return menu_items

# Post Menu Item
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.MenuItemResponse)
def createMenuItem(payload : schemas.MenuItem, db : Session = Depends(get_db)):

    new_item = models.MenuItem(**payload.dict())
    db.add(new_item)
    db.commit()

    # Getting new_item back from the database to return
    db.refresh(new_item)

    return new_item

# Get Menu Item By Its Id
@router.get('/{id}', response_model=schemas.MenuItemResponse)
def get_item_id(id : int, db : Session = Depends(get_db)):

    menu_item = db.query(models.MenuItem).filter(models.MenuItem.id == id).first()

    if not menu_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with id: {id} not found")

    return menu_item

# Get Menu Item By Its Category
@router.get('/category/{category}', response_model=List[schemas.MenuItemResponse])
def get_item_category(category : str, db: Session = Depends(get_db)):

    menu_items = db.query(models.MenuItem).filter(models.MenuItem.category == category).all()

    if not menu_items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with category: {category} not found")

    return menu_items

# Update Menu Item By Its Id

# Delete Menu Item By Its Id