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
    

