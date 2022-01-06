from pages.covid_international import covid_international
from pages.covid_spanish import covid_spanish
import streamlit as st


st.title("Welcome to Covid-19 Dashboard")
page = st.selectbox("Please select one page", ["Main Page","International","Spanish"])

if page == "International":
    covid_international()

if page == "Spanish":
    covid_spanish()
