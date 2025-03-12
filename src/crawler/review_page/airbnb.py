from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Accommodation_info:
    def __init__(self,driver):
        self.driver = driver

    def review_page(self,accommodation_id):
        self.driver.get(f'https://app.pineapples.com.br/channelmanager/accommodations/bk_airbnb?reference={accommodation_id}&detail={accommodation_id}')
    
    def review(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'channel__accommodations__detail__header__title')))
            scores = self.driver.find_elements(By.CLASS_NAME, 'accommodations-scores-preview__score')  
            if scores:
                return scores[0].text

            else: return 0
        except:
            return 'Not Found'

    def active(self):
        try:
            activated = self.driver.find_element(By.ID, 'connect').is_selected()
            if activated:
                if activated == True:
                    return True
                else: return 'Falso'
            else: 'Verificar'
        except: return 'Not Found'

    def accommodation_name(self):
        try:
            return self.driver.find_element(By.CLASS_NAME,'channel__accommodations__detail__header__title').text
        except: return 'Not Found'

    def account_perfil(self):
        try:
            time.sleep(5)
            perfil = self.driver.find_elements(By.CLASS_NAME,'cmpro-data-preview-item-value')
            if perfil:
                return self.driver.find_element(By.CLASS_NAME,'cmpro-data-preview-item-value').text ,self.driver.find_element(By.LINK_TEXT, 'Ver anúncio').get_attribute('href')
        except: return False

    def summarized_accommodation(self):
        if self.active() == True :
            perfil,link = self.account_perfil()
            return {'Accommodation_name':self.accommodation_name(),'Reviews':self.review(),'Perfil':perfil,'Link':link,'Status':self.active()}
        else: return {'Accommodation_name':self.accommodation_name(),'Reviews':None,'Perfil':None,'Link':None,'Status':self.active()}