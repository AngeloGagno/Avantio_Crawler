from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

class Connection:
    def __init__(self):
        self.con_string = self.get_connection_string()
        self.engine = self.create_engine() 

    def get_connection_string(self):
        load_dotenv(override=True)
        return os.getenv('DATABASE_URL')

    def create_engine(self):
        return create_engine(self.con_string)
