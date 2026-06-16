from fastapi import FastAPI
from routes.users import router as user_router 
from routes.expenses import router as expenses_router 
from db.database import Base, engine

app = FastAPI()


app.include_router(user_router)
app.include_router(expenses_router)


Base.metadata.create_all(bind=engine)