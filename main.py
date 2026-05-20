from Sources import API_1 , API_2
from utils import data_cleaning_api1
import json
import pandas as pd


api1=API_1.nif_API()
api2=API_2.invesG_API()

# print(api2)
# print(api1)

cleaned_list=[]


# print(json.dumps(api1, indent=4))

# print(data_cleaning_api1.clean_data(api1))

## fail safe to check if api call returns proper output
while api1.get("result")==0:
    api1=API_1.nif_API()

for data in api1.get("resultData"):
    data=data_cleaning_api1.clean_data(data)
    cleaned_list.append(data)

print(json.dumps(cleaned_list,indent=4,default=str))