from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    def __init__(self):
        """Instancia o driver do selenium passando suas configurações"""
        options = Options()
        options.add_argument("--headless") # Roda sem abrir o navegador (modo invisível)
        options.add_argument("--disable-gpu")  # Para sistemas Windows
        options.add_argument("--window-size=1920,1080")  # Tamanho da tela virtual (opcional)
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=options)

    def get_driver(self):
        """Getter para chamar o driver"""
        return self.driver