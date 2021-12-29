from fastapi import FastAPI

app = FastAPI()


# To run:
# uvicorn main:app

# To run in develop mode:
# uvicorn main:app --reload


# Un endpoint será una función.

@app.get("/")
async def root():
    return {"message": "Hola"}

@app.get("/hello/{name}")
async def salute(name):
    return {"message": f"Hola, {name}"}

@app.get("/hello/{name}/{age}")
async def person(name, age):
    return {"name": {"value": name,"type" : str(type(name))},
            "age": {"value": age,"type" : str(type(age))}}
            