from database.connect import Connection
import pandas as pd

def query():
    """Realiza a query desejada no banco"""
    return pd.read_sql("SELECT id_acc from accommodation a where a.status = 'ENABLED'",con=Connection().engine)
