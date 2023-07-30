from fastapi import FastAPI
from database.session import engine, SessionLocal
from routes import user
from models import models

app = FastAPI()

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