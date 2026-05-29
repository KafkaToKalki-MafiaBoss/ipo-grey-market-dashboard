import requests
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

def nif_API():
    try:
        url=st.secrets["nif_api"]
    except:
        url=os.getenv("nif_api")
    res=requests.get(url)
    return res.json()