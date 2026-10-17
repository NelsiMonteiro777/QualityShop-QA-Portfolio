from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_com_sucesso():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert "/inventory.html" in driver.current_url
    finally:
        driver.quit()

def test_login_sem_usuario():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "login-button").click()
        mensagem = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Epic sadface: Username is required" in mensagem
    finally:
        driver.quit()
def test_login_sem_password():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "login-button").click()
        mensagem = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Epic sadface: Password is required" in mensagem
    finally:
        driver.quit()
def test_login_username_invalido():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        mensagem = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Epic sadface: Username and password do not match any user in this service" in mensagem
    finally:
        driver.quit()
def test_login_password_invalida():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("senha_invalida")
        driver.find_element(By.ID, "login-button").click()
        mensagem = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert mensagem != ""
        assert "/inventory.html" not in driver.current_url
    finally:
        driver.quit()
def test_login_usuario_bloqueado():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        mensagem = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Epic sadface: Sorry, this user has been locked out." in mensagem
    finally:
        driver.quit()
def test_login_problem_user():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("problem_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert "/inventory.html" in driver.current_url
    finally:
        driver.quit()
        