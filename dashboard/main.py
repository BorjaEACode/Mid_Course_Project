from pages.covid_international import covid_international
from pages.covid_spanish import covid_spanish
import streamlit as st


st.set_page_config(layout="wide")
st.title("Welcome to Covid-19 Dashboard")
page = st.sidebar.radio("Page selected", ["Main Page","International","Spanish"])

if page == "Main Page":
    st.header("This Dashboard will provide you a full disclosured information about Covid-19 in Spain and worldwide")
    st.text("Please select one page at the sidebar")

if page == "International":
    covid_international()

if page == "Spanish":
    covid_spanish()
