from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Pet(BaseModel):
    id: int
    name: str
    status: str
    tags: list[str] = []

class NewPet(BaseModel):
    name: str
    status: str
    tags: list[str] = []

class UpdatePet(BaseModel):
    name: str
    status: str

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

@app.post('/pet')
def add_pet(pet: NewPet):
    pet_id = pets[-1].id + 1 if pets else 1
    new_pet = Pet(id=pet_id, **pet.dict())
    pets.append(new_pet)
    return new_pet

@app.put("/pet")
def update_pet(pet: Pet):
    pet_index = None
    for i, p in enumerate(pets):
        if p.id == pet.id:
            pet_index = i
            break
    else:
        return {"detail": "Pet not found."}
    pets[pet_index] = pet
    return pet

@app.get('/pet/{pet_id}')
def get_pet_by_id(pet_id: int):
    for p in pets:
        if p.id == pet_id:
            return p
    return {'detail':'pet not found.'}

@app.get("/pet/findByStatus")
def find_pets_by_status(status: str = "available"):
    results = [p for p in pets if p.status == status]
    return results

@app.get("/pet/findByTags")
def find_pets_by_tags(tags: list[str]):
    results = []
    for p in pets:
        if set(tags) <= set(p.tags):
            results.append(p)
    return results