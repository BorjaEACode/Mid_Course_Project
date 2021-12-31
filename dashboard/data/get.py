from config.api import url
import requests

def get_country_list():
    return requests.get(url+"/covid_internacional/country_list").json()

def get_country_coord(country):
    return requests.get(url+f"/covid_internacional/coord/{country}").json()

def get_country_data(country,data):
    return requests.get(url+f"/covid_internacional/data/{country}/{data}").json()
