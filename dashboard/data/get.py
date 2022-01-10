from config.api import url
import requests

def get_country_list():
    return requests.get(url+"/covid_internacional/country_list").json()

def get_country_coord(country):
    return requests.get(url+f"/covid_internacional/coord/{country}").json()

def get_country_all_data(country):
    return requests.get(url+f"/covid_internacional/all_data/{country}").json()

def get_country_data(country,data):
    return requests.get(url+f"/covid_internacional/data/{country}/{data}").json()

def get_country_data_date(country,data,date):
    return requests.get(url+f"/covid_internacional/date_data/{country}/{data}/{date}").json()

def get_country_all_data_date(country,date):
    return requests.get(url+f"/covid_internacional/date_all_data/{country}/{date}").json()

def get_country_data_between_date(country, data, date1, date2):
    return requests.get(url+f"/covid_internacional/between_date_data/{country}/{data}/{date1}/{date2}").json()
