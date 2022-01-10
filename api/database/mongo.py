from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("API_USER")
password = os.getenv("API_PASS")

url = f"mongodb+srv://{username}:{password}@cluster0.gnfmn.mongodb.net"

db = MongoClient(url).get_database("Covid")
