import psycopg2
import logging
import os
from dotenv import load_dotenv
import traceback

load_dotenv()

def data_insert(cleaned_data:list):
    try:
        db_url=os.getenv("db_url")
        conn=psycopg2.connect(db_url)
        c=conn.cursor()
        c.executemany("""
        INSERT INTO gmp_data (
            ipo_price, gmp_price, lot_size, estimated_listing_price, 
            estimated_listing_percentage, total_issue_price, company_name, 
            ipo_type, gmp_percentage, start_date, end_date, listing_date, 
            last_update, scraped_at
        )
        VALUES (
            %(ipo_price)s, %(gmp_price)s, %(lot_size)s, %(estimated_listing_price)s, 
            %(estimated_listing_percentage)s, %(total_issue_price)s, %(company_name)s, 
            %(ipo_type)s, %(gmp_percentage)s, %(start_date)s, %(end_date)s, %(listing_date)s, 
            %(last_update)s, %(scraped_at)s
        )
        ON CONFLICT (company_name, ipo_type, scraped_at) DO NOTHING;""", cleaned_data)

        print(f"rowcount: {c.rowcount}")
        logging.info(f"""Successfully added {c.rowcount} rows in the table
            from {len(cleaned_data)} entries provided""")

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"ERROR: {e}")
        traceback.print_exc()