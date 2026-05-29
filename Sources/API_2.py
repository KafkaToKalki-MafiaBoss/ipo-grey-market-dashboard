import requests
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def invesG_API():
    try:
        url=st.secrets["inves_api"]
    except:
        url=os.getenv("inves_api")
    res=requests.get(url)
    return res.json()