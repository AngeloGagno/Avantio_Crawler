from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

class AccommodationInfo:
    def __init__(self, driver):
        """Instancia o driver fornecido pelo usuário."""
        self.driver = driver

    def review_page(self, accommodation_id, portal):
        """Acessa a página de propriedades que contém os reviews e apartamentos ativos no portal selecionado."""
        url = (
            f'https://app.pineapples.com.br/channelmanager/accommodations/bk_{portal}'
            f'?reference={accommodation_id}&detail={accommodation_id}'
        )
        self.driver.get(url)

    def accommodation_name(self):
        """Retorna o nome da acomodação, ou 'Not Found' caso não seja encontrada."""
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'channel__accommodations__detail__header__title'))
            )
            return element.text
        except (NoSuchElementException, TimeoutException):
            return 'Not Found'

    def review(self):
        """
        Extrai a quantidade de reviews:
        - Retorna o número de reviews se encontrados.
        - Retorna 0 se não houver reviews.
        - Retorna 'Not Found' se a acomodação não existir.
        """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'channel__accommodations__detail__header__title'))
            )
            scores = self.driver.find_elements(By.CLASS_NAME, 'accommodations-scores-preview__score')
            if scores:
                return scores[0].text
            return 0
        except (NoSuchElementException, TimeoutException):
            return 'Not Found'

    def active(self):
        """
        Verifica se a propriedade está ativa no airbnb:
        - Retorna True se ativa.
        - Retorna 'Verificar' se não puder determinar.
        - Retorna 'Not Found' se não encontrar o elemento.
        """
        try:
            # Aguarda o elemento aparecer (caso necessário)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'connect'))
            )
            activated = self.driver.find_element(By.ID, 'connect').is_selected()
            return activated
        except (NoSuchElementException, TimeoutException):
            return 'Not Found'

    def account_profile(self):
        """
        Descobre qual perfil a propriedade se encontra:
        - Retorna uma tupla (perfil, link).
        - Retorna None se não encontrar.
        """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'cmpro-data-preview-item-value'))
            )
            perfil_element = self.driver.find_element(By.CLASS_NAME, 'cmpro-data-preview-item-value')
            link_element = self.driver.find_element(By.LINK_TEXT, 'Ver anúncio')
            
            perfil = perfil_element.text
            link = link_element.get_attribute('href')

            return perfil, link
        except (NoSuchElementException, TimeoutException):
            return None

    def summarized_accommodation(self) -> dict:
        """
        Resumo com informações da acomodação:
        - Se ativa, tenta buscar perfil e link.
        - Se não ativa, envia status e reviews.
        """
        name = self.accommodation_name()
        active_status = self.active()
        reviews_count = self.review()

        result = {
            'Accommodation_name': name,
            'Reviews': reviews_count,
            'Perfil': None,
            'Link': None,
            'Status': active_status
        }

        if active_status is True:
            profile_data = self.account_profile()
            if profile_data:
                perfil, link = profile_data
                result['Perfil'] = perfil
                result['Link'] = link

        return result
