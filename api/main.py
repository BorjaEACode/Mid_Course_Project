from fastapi import FastAPI
from .routers import covid_cases

app = FastAPI()


# To run:
# uvicorn main:app

# To run in develop mode:
# uvicorn main:app --reload


# Un endpoint será una función.

app.include_router(covid_cases.router)

@app.get("/")
async def root():
    return {"message": "Hola"}
