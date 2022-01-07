from config.api import url
import requests

def get_ccaa_list():
    return requests.get(url+"/covid_ccaa/list").json()

def get_ccaa_full_data(ccaa):
    return requests.get(url+f"/covid_ccaa/full_data/{ccaa}").json()

def get_ccaa_basic_data(ccaa):
    return requests.get(url+f"/covid_ccaa/basic_data/{ccaa}").json()
