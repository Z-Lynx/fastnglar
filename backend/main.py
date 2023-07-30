from fastapi import FastAPI
from database.session import engine, SessionLocal
from routes import user
from routes import auth
from models import models
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# create tables in the database
models.Base.metadata.create_all(bind=engine)

# dependency to get a database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# include routes for users and items
app.include_router(user.router)
app.include_router(auth.router)