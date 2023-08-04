from fastapi import FastAPI
from fastapi.responses import FileResponse
from database.session import engine, SessionLocal
from routes import user
from routes import auth
from models import models
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

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

# Define the list of allowed origins (you can customize this based on your needs)
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:4200",
]

# Add the CORS middleware to your FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/media", StaticFiles(directory="media"), name="media")

@app.get("/image/{filename}")
async def get_image(filename: str):
    # The file path will be /media/{filename}
    return FileResponse(f"media/image/{filename}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)