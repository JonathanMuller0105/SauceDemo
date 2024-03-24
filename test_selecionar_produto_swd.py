# 1 - Biblioteca
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe opcional
class Test_produtos():

# 2.1 Atributos 
    url = "https://www.saucedemo.com"

# 2.2 Funções e Métodos 
    def setup_method(self, method):                                               # método de inicialização dos testes 
        self.driver = webdriver.Chrome()                                          # Instancia o objeto do Selenium  Webdriver como chrome
        self.driver.implicitly_wait(15)                                           # Define o tempo de espera padrão por elementos em 10 segundos 

    def teardown_method(self, method):                                            # Médoto de finalização dos testes
        self.driver.quit()                                                        # Encerra / destroi o objeto do Selenium WebDriver da memória

    def test_selecionar_produto(self):                                            # Método de teste
        self.driver.get(self.url)                                                 # Abre o navegar
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")    # Escreve no campo user-name
        self.driver.find_element(By.NAME,"password").send_keys("secret_sauce")    # Escreve a senha
        self.driver.find_element(By.CSS_SELECTOR, "imput.submit-button.btn_action").click  # Executa a ação de clicar em entrar

# Transição de página
        
        assert self.driver.find_element(By.CSS_SELECTOR,".title").text =="Products"  # Confirma se esta escrito Products no elemento 
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack"  # Confirma se é a mochila
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.00"
