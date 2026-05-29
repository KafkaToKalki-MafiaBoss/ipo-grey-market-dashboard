import psycopg2
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def setup():
    try:
       db_url=st.secrets["db_url"]
    except:
       db_url=os.getenv("db_url")
    conn=psycopg2.connect(db_url)
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS gmp_data(
                                ipo_price FLOAT,
                                gmp_price FLOAT,
                                lot_size INTEGER,
                                estimated_listing_price FLOAT,
                                estimated_listing_percentage FLOAT,
                                total_issue_price FLOAT,
                                company_name TEXT,
                                ipo_type TEXT,
                                gmp_percentage FLOAT,
                                start_date TEXT,
                                listing_date TEXT,
                                last_update TEXT,
                                end_date TEXT,
                                scraped_at TEXT,
                                UNIQUE(company_name,ipo_type,scraped_at))''')


    conn.commit()
    conn.close()