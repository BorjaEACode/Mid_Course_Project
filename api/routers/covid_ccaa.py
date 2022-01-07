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

@router.get("/covid_ccaa/list")
def get_ccaa_list():
    results = list(db["Covid_Comunidades"].find({},{"Comunidad autónoma":1,"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/covid_ccaa/most_complete_vaccinated")
def get_ccaas_most_compl_vac():
    results = list(db["Covid_Comunidades"].find({},{"Comunidad autónoma": 1, "Porcentaje Pauta Completa": 1,"_id": 0}).sort("Porcentaje Pauta Completa", 1))
    return loads(json_util.dumps(results))

@router.get("/covid_ccaa/basic_data/{ccaa}")
def get_ccaa_basic_data(ccaa):
    results = list(db["Covid_Comunidades"].find({"Comunidad autónoma": ccaa},{"_id":0,"Comunidad autónoma":1,"Casos":1, "Fallecidos":1,"Población":1,"Total Pauta Completa":1,"Porcentaje Pauta Completa":1}))
    return loads(json_util.dumps(results))

@router.get("/covid_ccaa/full_data/{ccaa}")
def get_ccaa_full_data(ccaa):
    results = list(db["Covid_Comunidades"].find({"Comunidad autónoma": ccaa},{"_id":0, "Lat":0,"Long":0}))
    return loads(json_util.dumps(results))

@router.get("/covid_ccaa/{vaccine}/{positions}")
def get_vaccine_top_ccaas(vaccine,positions:int):
    results = list(db["Covid_Comunidades"].find({},{"Comunidad autónoma": 1,f"{vaccine.title()} Entregadas":1, "_id": 0}).limit(positions).sort(f"{vaccine.title()} Entregadas", -1))
    return loads(json_util.dumps(results))
