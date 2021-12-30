from fastapi import APIRouter
from ..database.mongo import db
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/covid")
def covid_root():
    return {
        "message": "Welcome to the covid Spain CCAA database"
    }

@router.get("/covid/ccaa_list")
def get_ccaa_list():
    results = list(db["Covid_Comunidades"].find({},{"Comunidad autónoma":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/covid/ccaa/{ccaa}")
def get_ccaa_data(ccaa):
    results = list(db["Covid_Comunidades"].find({"Comunidad autónoma": ccaa}))
    return loads(json_util.dumps(results))
