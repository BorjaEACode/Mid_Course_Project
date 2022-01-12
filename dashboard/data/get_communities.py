from config.api import URL
import requests

def get_ccaa_list():
    return requests.get(URL+"/covid_ccaa/list").json()

def get_ccaa_full_data(ccaa):
    return requests.get(URL+f"/covid_ccaa/full_data/{ccaa}").json()

def get_ccaa_basic_data(ccaa):
    return requests.get(URL+f"/covid_ccaa/basic_data/{ccaa}").json()
