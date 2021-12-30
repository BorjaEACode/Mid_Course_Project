from fastapi import APIRouter
from ..database.mongo import db
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/covid")
def covid_root():
    return {
        "message": "Welcome to the covid deaths database"
    }

@router.get("/covid/country_deaths_list")
def get_country_deaths_list():
    results = list(db["Covid_Deaths_Checked"].find({},{"Country/Region":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/covid/deaths/{country}")
def get_country_deaths(country):
    results = list(db["Covid_Deaths_Checked"].find({"Country/Region": country}))
    return loads(json_util.dumps(results))
