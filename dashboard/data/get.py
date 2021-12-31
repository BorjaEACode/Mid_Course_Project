from config.api import url
import requests

def get_list_country():
    return requests.get(url+"/covid_internacional/country_list").json()

def get_data_country(country,data):
    return requests.get(url+f"/covid_internacional/{country}/{data}").json()
