from crawler.login.frontpage import Login
from crawler.review_page.airbnb import Accommodation_info   
from crawler.driver import Driver
from database.query import query
import time
import pandas as pd

def dataframe(accomodation_instance):
    data = []
    df = query()
    for accommodation in range(0,len(df)):
        accomodation_instance.review_page(df.loc[accommodation,'id_acc'])
        time.sleep(5)
        data.append(accomodation_instance.summarized_accommodation())
        time.sleep(5)
    return data

def start_crawler(driver_instance):
    login_instance = Login(driver_instance)
    login_instance.connecting_page()
    login_instance.username()
    login_instance.password()

def fetch_all():
    driver_instance = Driver().get_driver()
    accomodation_instance = Accommodation_info(driver_instance)
    start_crawler(driver_instance)
    return dataframe(accomodation_instance)

def main(data):
    df = pd.DataFrame(data)
    df.to_excel('accommodations.xlsx', index=False)
    
if __name__ == '__main__':
    main(fetch_all())
