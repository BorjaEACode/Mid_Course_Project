from fastapi import APIRouter
from ..database.mongo import db
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/covid_internacional")
def covid_root():
    return {
        "message": "Welcome to the covid database"
    }

@router.get("/covid_internacional/country_list")
def get_country_list():
    results = list(db["Covid_Cases_Checked"].find({},{"Country/Region":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/covid_internacional/coord/{country}")
def get_country_coord(country):
    results = list(db[f"Covid_Cases_Checked"].find({"Country/Region": country.title()},{"Lat":1,"Long":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/covid_internacional/data/{country}/{data}")
def get_country_data(country, data):
    results = list(db[f"Covid_{data.title()}_Checked"].find({"Country/Region": country.title()},{"_id":0,"Lat":0,"Long":0,"Country/Region":0}))
    return loads(json_util.dumps(results))
