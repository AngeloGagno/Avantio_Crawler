from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

class Login:
    def __init__(self, driver):
        load_dotenv(override=True)
        self.driver = driver

    def connecting_page(self):
        self.driver.get('https://app.pineapples.com.br/')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'user_name')))  

    def username(self):
        username_field = self.driver.find_element(By.ID, 'user_name')
        username_field.send_keys(os.getenv('user_name'))

    def password(self):
        password_field = self.driver.find_element(By.ID, 'user_password')
        password_field.send_keys(os.getenv('user_password'))

        self.driver.find_element(By.ID, 'login_button').click()
        WebDriverWait(self.driver, 20).until(EC.url_changes("https://app.pineapples.com.br"))  
    
    
    


