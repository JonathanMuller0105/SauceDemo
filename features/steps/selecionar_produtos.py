# 1 - Bibliotecas / Imports
import time
from behave import given, when, then 
from selenium import webdriver
from selenium.webdriver.common.by import By



@given(u'que acesso o site Sauce Demo')
@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # Setup / Inicialização
    context.driver = webdriver.Chrome()               # Instanciar o objeto do Selenium Webdriver especializado para chrome
    context.driver.maximize_window()                  # Maximizar a janela do navegador
    context.driver.implicitly_wait(10)                # Esperar até 10 segundos por qualquer elemento 
    context.driver.get("https://www.saucedemo.com")   # vai abrir o navegador qno endereço do site alvo

# Preencher com usiarioe senha 
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)   # Preenche o Usuario
    context.driver.find_element(By.ID, "password"). send_keys(senha)     # Preenche  a senha
    context.driver.find_element(By.ID, "login-button").click()           #clicar no botão login 

# Preencher com usuário em branco e senha
@when(u'preencho os campos de login com usuario e senha {senha}')
def step_impl(context, usuario, senha):
    # não preenche o usuario
    context.driver.find_element(By.ID, "password"). send_keys(senha)     # Preenche  a senha
    context.driver.find_element(By.ID, "login-button").click()           #clicar no botão login 

# Preencher com usuário, mas deixar a senha em branco
@when(u'preencho os campos de login com usuario {usuario} e senha')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)   # Preenche o Usuario
    # não preenche a senha 
    context.driver.find_element(By.ID, "login-button").click()           #clicar no botão login 

# Clica no botão de login sem ter preenchico o usuátio e a senha 
@when(u'preencho os campos de login com usuario e senha')
def step_impl(context, usuario, senha):
    # não preenche o Usuario
    # não preenche  a senha
    context.driver.find_element(By.ID, "login-button").click()           #clicar no botão login 

# Preencher com usiarioe e senha através da decisão (IF)
@when(u'digito os campos de login com usuario {usuario} e senha {senha} com IF')
def step_impl(context, usuario, senha):
    if usuario != '<branco>':
        context.driver.find_element(By.ID, "user-name").send_keys(usuario)   # Preenche o Usuario
        # se o usuario estiver em branco não há ação de preenchimento

    if senha != '<branco':
        context.driver.find_element(By.ID, "password"). send_keys(senha)     # Preenche  a senha

    context.driver.find_element(By.ID, "login-button").click()           #clicar no botão login 

@then(u'sou direcionado para página Home')
def step_impl(context):
    #time.sleep(2)
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    #time.sleep(2)    # é uma espera por 02 segundo - remover depois = alfinete

    # teardown / Encerramento
    context.driver.quit()

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

    # teardown / Encerramento
    context.driver.quit()

    # Verifica mensagem de para Scenario Outline: Login Negativo
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem 

    # teardown / Encerramento
    context.driver.quit()
