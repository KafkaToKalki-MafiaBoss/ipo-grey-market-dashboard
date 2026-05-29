from Sources import API_1 , API_2
from utils import data_cleaning_api1
from database import db_setup,db_insert
import json
import logging

def run_pipeline():
    try:
        logging.info("Pipeline Started")
        api1=API_1.nif_API()
        api2=API_2.invesG_API()

        cleaned_list=[]

        ## fail safe to check if api call returns proper output
        for _ in range(5):
            if api1.get("result")==0:
                logging.info("API Call Failed Trying again")
                api1=API_1.nif_API()

        logging.info("""API Call Successful.
                        Initiating Data Preprocessing""")
        
        for data in api1.get("resultData"):
            data=data_cleaning_api1.clean_data(data)
            cleaned_list.append(data)


        db_setup.setup()
        db_insert.data_insert(cleaned_list)
    
    except Exception as e:
        logging.error(f"Exception occured {e}")