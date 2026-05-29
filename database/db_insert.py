import sqlite3
import logging

def data_insert(cleaned_data:list):
    conn=sqlite3.connect("data/ipo_gmp.db")
    c=conn.cursor()
    c.executemany("""INSERT OR IGNORE INTO 
                  gmp_data(ipo_price,gmp_price,lot_size,estimated_listing_price,estimated_listing_percentage,total_issue_price,company_name,ipo_type,gmp_percentage,start_date,end_date,listing_date,last_update,scraped_at)
                  VALUES(:ipo_price,:gmp_price,:lot_size,:estimated_listing_price,:estimated_listing_percentage,:total_issue_price,:company_name,:ipo_type,:gmp_percentage,:start_date,:end_date,:listing_date,:last_update,:scraped_at)""",cleaned_data)
    
    logging.info(f"""Successfully added {c.rowcount} rows in the table
          from {len(cleaned_data)} entries provided""")

    conn.commit()
    conn.close()