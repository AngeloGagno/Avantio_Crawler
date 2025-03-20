import pandas as pd
from execute_crawler import fetch_all,cleaning_portal
from load_sheets.send_to_sheets import update_sheets
import os
from dotenv import load_dotenv
import json

def main(data:json, sheet:str) -> None:
    load_dotenv(override=True)
    """Envia para o Sheets o retorno do Json criado na automação"""
    df = pd.DataFrame(data)
    update_sheets(os.getenv('SHEETS_ID'),sheet,df)
    
if __name__ == '__main__':
    main(fetch_all(),cleaning_portal())
