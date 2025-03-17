from crawler.login.frontpage import Login
from crawler.login.twoFA import TwoFactorAuthenticator
from crawler.review_page.review_scrap import AccommodationInfo   
from crawler.driver import Driver
from database.query import query
import argparse
import time

def dataframe(accomodation_instance:AccommodationInfo,portal:str) -> list:
    """Instancia o acesso a pagina de cada propriedade e verifica seus status de acordo com a classe Accommodation_info"""
    data = []
    df = query()
    for accommodation in range(183,len(df)):
        id_accommodation = df.loc[accommodation,'id_acc']
        accomodation_instance.review_page(id_accommodation,portal=portal)
        time.sleep(5)
        data.append(accomodation_instance.summarized_accommodation(accommodation_id=id_accommodation))
        time.sleep(5)
    return data

def start_crawler(driver_instance:Driver) -> None:
    """Instancia os passos para realização do login e autenticação 2FA se necessário."""
    Login(driver_instance)
    two_fa = TwoFactorAuthenticator(driver_instance)
    time.sleep(2)
    if two_fa.check_page():
        two_fa.run_2fa() 
        time.sleep(1)
        Login(driver_instance)

def set_portal() -> str:
    parser = argparse.ArgumentParser(description='Portal')
    parser.add_argument('--portal',type=str,help='Digite o portal desejado(airbnb ou bookingcom)',default='airbnb')
    args = parser.parse_args()
    return args.portal  

def fetch_all() -> list:
    """Faz o login na avantio e verifica o acesso a pagina de cada propriedade,
    seus status de acordo com a classe Accommodation_info """
    portal = set_portal()
    driver_instance = Driver().get_driver()
    accomodation_instance = AccommodationInfo(driver_instance)
    start_crawler(driver_instance)
    return dataframe(accomodation_instance,portal)
