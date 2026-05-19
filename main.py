from Sources import API_1 , API_2
from utils import data_cleaning_api1


api1=API_1.nif_API()
api2=API_2.invesG_API()

# print(api2)
# print(api1)

import json

# print(json.dumps(api1, indent=4))

print(data_cleaning_api1.clean_data(json.dumps(api1, indent=4)))