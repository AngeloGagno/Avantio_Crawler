from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
class Accommodation_info:
    def __init__(self,driver):
        """Instancia o driver fornecido pelo usuario"""
        self.driver = driver

    def review_page(self,accommodation_id):
        """Acessa a página de propriedades que contem os reviews e apartamentos que estao ativos no airbnb"""
        self.driver.get(f'https://app.pineapples.com.br/channelmanager/accommodations/bk_airbnb?reference={accommodation_id}&detail={accommodation_id}')
    
    def review(self):
        """Extrai a quantidade de reviews caso não tenha retorna 0, 
        em caso de erro de nao possuir o apartamento retorna a string 'NOT FOUND'
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'channel__accommodations__detail__header__title')))
            scores = self.driver.find_elements(By.CLASS_NAME, 'accommodations-scores-preview__score')  
            if scores:
                return scores[0].text

            else: return 0
        except:
            return 'Not Found'

    def active(self):
        """Verifica se a propriedade está ativa no airbnb, há a possibilidade
        do aparecimento a mensagem 'Tentar novamente', caso apareça essa mensagem é retornado
        a mensagem Verificar. Caso Erro a mensagem Not Found é enviada
        """
        try:
            activated = self.driver.find_element(By.ID, 'connect').is_selected()
            if activated:
                if activated == True:
                    return True
                else: return 'Falso'
            else: 'Verificar'
        except: return 'Not Found'

    def accommodation_name(self):
        """Retorna o nome da acomodação, caso nao seja encontrada apresenta a mensagem Not Found"""
        try:
            return self.driver.find_element(By.CLASS_NAME,'channel__accommodations__detail__header__title').text
        except: return 'Not Found'

    def account_perfil(self):
        """Descobre qual perfil a propriedade se encontra"""
        try:
            time.sleep(5)
            perfil = self.driver.find_elements(By.CLASS_NAME,'cmpro-data-preview-item-value')
            if perfil:
                return self.driver.find_element(By.CLASS_NAME,'cmpro-data-preview-item-value').text ,self.driver.find_element(By.LINK_TEXT, 'Ver anúncio').get_attribute('href')
        except: return False

    def summarized_accommodation(self) -> json:
        """Une todas as funções e envia em formato JSON"""
        if self.active() == True :
            perfil,link = self.account_perfil()
            return {'Accommodation_name':self.accommodation_name(),'Reviews':self.review(),'Perfil':perfil,'Link':link,'Status':self.active()}
        else: return {'Accommodation_name':self.accommodation_name(),'Reviews':self.review(),'Perfil':None,'Link':None,'Status':self.active()}