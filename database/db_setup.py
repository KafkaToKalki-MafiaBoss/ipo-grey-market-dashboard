import sqlite3

conn=sqlite3.connect("data.db")
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS customers(
                            ipo_id INTEGER,
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
                            scraped_at TEXT,
                            UNIQUE(company_name,ipo_type,scraped_at))''')


conn.commit()
conn.close
