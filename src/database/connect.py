from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

class Connection:
    """Cria uma conexão com o banco de dados"""
    def __init__(self):
        self.con_string = self.get_connection_string()
        self.engine = self.create_engine() 

    def get_connection_string(self):
        """Retorna a string de conexão com o banco"""
        load_dotenv(override=True)
        return os.getenv('DATABASE_URL')

    def create_engine(self):
        """Cria a conexão com o banco"""
        return create_engine(self.con_string)
