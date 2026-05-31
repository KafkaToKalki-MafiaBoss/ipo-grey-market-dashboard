import requests
import os
from dotenv import load_dotenv

load_dotenv()

def nif_API():
    url=os.getenv("nif_api")
    res=requests.get(url)
    return res.json()