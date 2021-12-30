from fastapi import FastAPI

from api.routers import covid_ccaa, covid_deaths, covid_recovered
from .routers import covid_cases

app = FastAPI()


# To run:
# uvicorn main:app

# To run in develop mode:
# uvicorn main:app --reload


# Un endpoint será una función.

app.include_router(covid_cases.router)
app.include_router(covid_deaths.router)
app.include_router(covid_recovered.router)
app.include_router(covid_ccaa.router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la database sobre Covid-19"}
