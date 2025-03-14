from crawler.login.frontpage import Login
from crawler.login.twoFA import TwoFactorAuthenticator
from crawler.review_page.review_scrap import AccommodationInfo   
from crawler.driver import Driver
from database.query import query
import time
import pandas as pd


def dataframe(accomodation_instance):
    """Instancia o acesso a pagina de cada propriedade e verifica seus status de acordo com a classe Accommodation_info"""
    data = []
    df = query()
    for accommodation in range(0,len(df)):
        accomodation_instance.review_page(df.loc[accommodation,'id_acc'],portal='bookingcom')
        time.sleep(5)
        data.append(accomodation_instance.summarized_accommodation())
        time.sleep(5)
    return data

def start_crawler(driver_instance):
    """Instancia os passos para realização do login e autenticação 2FA se necessário."""
    Login(driver_instance)
    two_fa = TwoFactorAuthenticator(driver_instance)
    time.sleep(2)
    if two_fa.check_page():
        two_fa.run_2fa() 
        time.sleep(1)
        Login(driver_instance)

def fetch_all() -> list:
    """Faz o login na avantio e verifica o acesso a pagina de cada propriedade,
    seus status de acordo com a classe Accommodation_info """
    driver_instance = Driver().get_driver()
    accomodation_instance = AccommodationInfo(driver_instance)
    start_crawler(driver_instance)
    return dataframe(accomodation_instance)

def main(data):
    """Envia para o Excel o retorno do Fetch_all"""
    df = pd.DataFrame(data)
    df.to_excel('accommodations.xlsx', index=False)
    
if __name__ == '__main__':
    main(fetch_all())
