import requests

def nif_API():
    url="https://webapi.niftytrader.in/webapi/Ipo/gmp-list"
    res=requests.get(url)
    return res.json()

# function to reverse a list