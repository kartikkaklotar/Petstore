from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Pet(BaseModel):
    id: int
    name: str
    status: str
    tags: list[str] = []

## Mock Data
pets = [
    Pet(id=1, name="Fluffy", status="available", tags=["cat"]),
    Pet(id=2, name="Buddy", status="pending", tags=["dog"]),
    Pet(id=3, name="Charlie", status="sold", tags=["dog"])
]

@app.get('/')
def root():
    return {"Message":"Hello World!"}

@app.get('/pets')
def get_pets():
    return pets
