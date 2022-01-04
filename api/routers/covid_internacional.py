from datetime import date, datetime
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
    results = list(db["Covid_Cases_OK"].find({},{"Country/Region":1,"_id":0}).distinct("Country/Region"))
    return loads(json_util.dumps(results))

@router.get("/covid_internacional/coord/{country}")
def get_country_coord(country):
    results = list(db["Covid_Location"].find({"Country/Region": country},{"Lat":1,"Long":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/covid_internacional/data/{country}/{data}")
def get_country_data(country, data):
    results = list(db[f"Covid_{data.title()}_OK"].find({"Country/Region": country},{"Country/Region":0,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/covid_internacional/date_data/{country}/{data}/{date}")
def get_country_data_date(country, data, date:date):
    date_str = date.strftime("%-m/%d/%y")
    results = list(db[f"Covid_{data.title()}_OK"].find({"Country/Region": country, "Date": date_str},{"value":1,"Date":1,"Country/Region":1,"_id":0}))
    return loads(json_util.dumps(results))
    