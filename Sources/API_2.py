import requests
import os
from dotenv import load_dotenv

load_dotenv()

def invesG_API():
    url=os.getenv("inves_api")
    res=requests.get(url)
    return res.json()