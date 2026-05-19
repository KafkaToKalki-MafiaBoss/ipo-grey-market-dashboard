import re
from datetime import datetime

def clean_data(raw):
    def company_name_clean(name: str)->str:
        return name.replace(" IPO","").strip()
    
    def parse_currency(value: str)->float:
        if not value:
            return None
        value.replace("₹","").replace("\u20b9","").strip()
        return float(re.sub(r"[^\d.]","",value))
    
    def parse_percentage(value: str)->float:
        if not value:
            return None
        value.replace("%","").strip()
        return float(value)
    
    def parse_issue_price(value:str)->float:
        if not value:
            return None
        return float(re.sub(r"[\d.]","",value))*(10000000 if "Cr" in value else 1)
    
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
            return datetime.fromisoformat(date_str)
        except ValueError:
            pass
        
        for format in formats_to_try:
            try:
                return datetime.strptime(date_str.strip(),format)
            except ValueError:
                continue
        
        return None
    
    def normalize_record(raw:dict)->dict:
        return {
            "ipo_id":raw.get("ipo_id"),
            "ipo_price":raw.get("ipo_price"),
            "gmp_price":parse_currency(raw.get("gmp_price")),
            "lot_size":raw.get("lot_size"),
            "estimated_listing_price":parse_currency(raw.get("estimated_listing_price")),
            "estimated_listing_percentage":parse_percentage(raw.get("estimated_listing_percentage")),
            "total_issue_price":parse_issue_price(raw.get("total_issue_price")),
            "company_name":company_name_clean(raw.get("company_name")),
            "ipo_type":raw.get("ipo_type"),
            "gmp_percentage":100*(parse_currency(raw.get("gmp_price"))/raw.get("ipo_price")),
            "start_date":parse_date(raw.get("start_date")),
            "end_date":parse_date(raw.get("end_date")),
            "listing_date":parse_date(raw.get("listing_date")),
            "last_update":parse_date(raw.get("last_update")),
            }
    normalize_record(raw)