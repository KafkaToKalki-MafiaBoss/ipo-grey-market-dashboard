import sqlite3
def setup():
    conn=sqlite3.connect("data/ipo_gmp.db")
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS gmp_data(
                                ipo_price REAL,
                                gmp_price REAL,
                                lot_size INTEGER,
                                estimated_listing_price REAL,
                                estimated_listing_percentage REAL,
                                total_issue_price REAL,
                                company_name TEXT,
                                ipo_type TEXT,
                                gmp_percentage REAL,
                                start_date TEXT,
                                listing_date TEXT,
                                last_update TEXT,
                                end_date TEXT,
                                scraped_at TEXT,
                                UNIQUE(company_name,ipo_type,scraped_at))''')


    conn.commit()
    conn.close()