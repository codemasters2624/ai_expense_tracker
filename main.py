from fastapi import FastAPI
from routes.users import router as user_router
from db.database import Base, engine
from db.models import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)