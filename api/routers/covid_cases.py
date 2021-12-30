from fastapi import APIRouter
from ..database.mongo import db
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/covid")
def covid_root():
    return {
        "message": "Welcome to the covid cases database"
    }

@router.get("/covid/cases/country_list")
def get_country_list():
    results = list(db["Covid_Cases_Checked"].find({},{"Country/Region":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/covid/cases/{country}")
def get_country_cases(country):
    results = list(db["Covid_Cases_Checked"].find({"Country/Region": country}))
    return loads(json_util.dumps(results))


