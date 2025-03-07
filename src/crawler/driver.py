from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login.frontpage import Login
from review_page.airbnb import Accommodation_info
import time

class Driver:
    def __init__(self):
        
        options = Options()
        options.add_argument("--start-maximized")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=options)

    def get_driver(self):
        return self.driver
    

if __name__ == '__main__':
    driver_instance = Driver().get_driver()
    login_instance = Login(driver_instance)
    accomodation_instance = Accommodation_info(driver_instance)

    login_instance.connecting_page()
    login_instance.username()
    login_instance.password()
    time.sleep(2)
    accomodation_instance.review_page(accommodation_id='407540')
    time.sleep(10)
    print(accomodation_instance.summarized_accommodation())
