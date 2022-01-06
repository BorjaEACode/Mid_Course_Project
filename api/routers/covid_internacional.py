from datetime import datetime
from fastapi import APIRouter
from ..database.mongo import db
from bson import json_util
from json import loads
from datetime import datetime 

router = APIRouter()

@router.get("/covid_internacional")
def covid_root():
    return {
        "message": "Welcome to the covid database"
    }

@router.get("/covid_internacional/country_list")
def get_country_list():
    results = list(db["Covid_Data"].find({},{"Country/Region":1,"_id":0}).distinct("Country/Region"))
    return loads(json_util.dumps(results))

@router.get("/covid_internacional/coord/{country}")
def get_country_coord(country):
    results = list(db["Covid_Location"].find({"Country/Region": country},{"Lat":1,"Long":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/covid_internacional/data/{country}/{data}")
def get_country_data(country, data):
    results = list(db["Covid_Data"].find({"Country/Region": country},{"Country/Region":1, "Date":1, f"{data}":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/covid_internacional/date_data/{country}/{data}/{date}")
def get_country_data_date(country, data, date):
    if type(date)==str:
        date = datetime.strptime(date,"%Y-%m-%d")
    else:
        date=date
    results = list(db["Covid_Data"].find({"Country/Region": country, "Date": date},{"Country/Region":1,"Date":1,f"{data}":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/covid_internacional/between_date_data/{country}/{data}/{date1}/{date2}")
def get_country_data_between_date(country, data, date1, date2):
    if type(date1)==str:
        date1 = datetime.strptime(date1,"%Y-%m-%d")
        date2 = datetime.strptime(date2,"%Y-%m-%d")
    else:
        date1=date1
        date2=date2
    results = list(db["Covid_Data"].find({"Country/Region": country, "Date":{"$gte":date1, "$lte":date2}},
    {"Country/Region":1,f"{data}":1,"Date":1,"_id":0}))
    return loads(json_util.dumps(results))
    