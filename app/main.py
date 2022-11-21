from . import models
from .database import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import post, user, auth, vote
from .config import settings

# models.Base.metadata.create_all(bind=engine) # use to create the tables without alembic

origins = ["*"]  # secure which website can access my API.

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World !"}


#    10h37 : https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/
# uvicorn app.main:app --reload
# c:/Users/Guillaume/Documents/code/fastapi/venv/Scripts/Activate.ps1
