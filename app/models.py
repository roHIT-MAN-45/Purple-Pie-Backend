from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null, text
from sqlalchemy import Column, Integer, String, Boolean, Float, TIMESTAMP, ForeignKey

# User Model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String, nullable = False)
    phone = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))


# MenuItems Model
class MenuItem(Base):
    __tablename__ = "menuitems"

    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String, nullable = False)
    category = Column(String, nullable = False)
    itemType = Column(String, nullable = False)
    description = Column(String, nullable = False)
    price = Column(Float, nullable = False)
    calories = Column(Integer, nullable = False)
    isFavourite = Column(Boolean, server_default = 'False', nullable = False)
    image = Column(String, nullable = False)