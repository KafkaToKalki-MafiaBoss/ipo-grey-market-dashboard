import requests

def invesG_API():
    url="https://webnodejs.investorgain.com/cloud/new/report/data-read/331/1/3/2026/2025-26/0/all?search=&v=16-18"
    res=requests.get(url)
    return res.json()