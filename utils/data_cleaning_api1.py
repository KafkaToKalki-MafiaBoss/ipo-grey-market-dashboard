import re
from datetime import datetime

def clean_data(raw:dict)->dict:
    def company_name_clean(name: str)->str:
        if not name:
            return None
        return name.replace(" IPO","").strip()
    
    def parse_currency(value: str)->float:
        if not value:
            return None
        
        a=value.replace("\u20b9","").strip()
        if a=="":
            return None
        else:
            return float(re.sub(r"[^\d.]","",a))
    
    def parse_percentage(value: str)->float:
        if not value:
            return None
        
        return float(value.replace("%","").strip())
    
    def parse_issue_price(value:str)->float:
        if not value:
            return None
        return float(re.sub(r"[^\d.]","",value))*(10000000 if "Cr" in value else 1)
    
    def parse_date(date_str:str):
        if not date_str:
            return None
        formats_to_try = [
        "%Y-%m-%d",           
        "%d-%m-%Y",            
        "%d/%m/%Y",        
        "%B %d, %Y",           
        "%b %d, %Y"     ]
    
        try:
            return datetime.strftime(datetime.fromisoformat(date_str))
        except ValueError:
            pass
        
        for format in formats_to_try:
            try:
                return datetime.strftime(datetime.strptime(date_str.strip(),format))
            except ValueError:
                continue
        
        return None
    
    def gmp_percentage(gmp_price,ipo_price):
        if ipo_price is not None and gmp_price is not None:
            if ipo_price==0:
                return None
            return 100*(gmp_price/ipo_price)
        return None
    
    def normalize_record(raw:dict)->dict:
        return {
            "ipo_id":raw.get("ipo_id"),
            "ipo_price":raw.get("ipo_price"),
            "gmp_price":raw.get("gmp_price"),
            "lot_size":raw.get("lot_size"),
            "estimated_listing_price":parse_currency(raw.get("estimated_listing_price")),
            "estimated_listing_percentage":parse_percentage(raw.get("estimated_listing_percentage")),
            "total_issue_price":parse_issue_price(raw.get("total_issue_price")),
            "company_name":company_name_clean(raw.get("company_name")),
            "ipo_type":raw.get("type"),
            "gmp_percentage":gmp_percentage(raw.get("gmp_price"),raw.get("ipo_price")),
            "start_date":parse_date(raw.get("start_date")),
            "end_date":parse_date(raw.get("end_date")),
            "listing_date":parse_date(raw.get("listing_date")),
            "last_update":parse_date(raw.get("last_update")),
            "scraped_at":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    return normalize_record(raw)