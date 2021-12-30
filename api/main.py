from fastapi import FastAPI
from .routers import covid_internacional, covid_ccaa

app = FastAPI()


# To run:
# uvicorn main:app

# To run in develop mode:
# uvicorn main:app --reload


# Un endpoint será una función.

app.include_router(covid_internacional.router)
app.include_router(covid_ccaa.router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la database sobre Covid-19"}
