from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

class Login:
    def __init__(self, driver):
        """Instancia a classe para realizar o login no site da avantio"""
        load_dotenv(override=True)
        self.driver = driver
        self.connect = self.connecting_page()
        self.user = self.username()
        self.password = self.password()
        
    def connecting_page(self):
        """Acessa a pagina da pineapples"""
        self.driver.get('https://app.pineapples.com.br/')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'user_name')))  

    def username(self):
        """Fornece a credencial usuario"""
        username_field = self.driver.find_element(By.ID, 'user_name')
        username_field.send_keys(os.getenv('user_name'))

    def password(self):
        """Fornece as credenciais senha"""
        password_field = self.driver.find_element(By.ID, 'user_password')
        password_field.send_keys(os.getenv('user_password'))

        self.driver.find_element(By.ID, 'login_button').click()
        WebDriverWait(self.driver, 20).until(EC.url_changes("https://app.pineapples.com.br"))  
    
    



