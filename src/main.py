from crawler.login.frontpage import Login
from crawler.review_page.airbnb import Accommodation_info   
from crawler.driver import Driver
from database.query import query
import time
def main():
    driver_instance = Driver().get_driver()
    login_instance = Login(driver_instance)
    accomodation_instance = Accommodation_info(driver_instance)
    login_instance.connecting_page()
    login_instance.username()
    login_instance.password()
    time.sleep(2)
    accomodation_instance.review_page(accommodation_id='328164')
    time.sleep(5)
    accomodation_instance.summarized_accommodation()