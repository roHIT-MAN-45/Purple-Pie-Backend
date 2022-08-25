from fastapi import FastAPI
from . import models
from .database import engine
from . routers import user, auth, menuItems

# CORS Module
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

# Creating instance of FastAPI
app = FastAPI()

# Allowing CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message" : "Hello Frontend ⚡"}

# User
app.include_router(user.router)

# Authentication
app.include_router(auth.router)

# Menu Items
app.include_router(menuItems.router)
