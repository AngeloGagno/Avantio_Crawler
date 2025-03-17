import pandas as pd
from execute_crawler import fetch_all
import json

def main(data:json) -> None:
    """Envia para o Excel o retorno do Json criado na automação"""
    df = pd.DataFrame(data)
    df.to_excel('accommodations.xlsx', index=False)
    
if __name__ == '__main__':
    main(fetch_all())
