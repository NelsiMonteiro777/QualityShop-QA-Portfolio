from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_adicionar_produto_ao_carrinho():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        botao = driver.find_element(By.ID, "remove-sauce-labs-backpack").text
        contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

        assert botao == "Remove"
        assert contador == "1"
    finally:
        driver.quit()

def test_verificar_produto_no_carrinho():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        botao_adicionar = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        )
        produto_products = botao_adicionar.find_element(
            By.XPATH, "./ancestor::div[contains(@class, 'inventory_item')]"
        )
        nome_products = produto_products.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text
        descricao_products = produto_products.find_element(
            By.CLASS_NAME, "inventory_item_desc"
        ).text
        preco_products = produto_products.find_element(
            By.CLASS_NAME, "inventory_item_price"
        ).text

        botao_adicionar.click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        item_carrinho = driver.find_element(By.CLASS_NAME, "cart_item")
        quantidade = item_carrinho.find_element(
            By.CLASS_NAME, "cart_quantity"
        ).text
        nome_carrinho = item_carrinho.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text
        descricao_carrinho = item_carrinho.find_element(
            By.CLASS_NAME, "inventory_item_desc"
        ).text
        preco_carrinho = item_carrinho.find_element(
            By.CLASS_NAME, "inventory_item_price"
        ).text

        assert quantidade == "1"
        assert nome_carrinho == nome_products
        assert descricao_carrinho == descricao_products
        assert preco_carrinho == preco_products
    finally:
        driver.quit()

def test_remover_produto_do_carrinho():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

        itens = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(itens) == 0
    finally:
        driver.quit()

def test_continuar_a_comprar():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "continue-shopping").click()

        assert "/inventory.html" in driver.current_url
    finally:
        driver.quit()

def test_acessar_checkout_pelo_carrinho():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        assert "checkout-step-one.html" in driver.current_url
    finally:
        driver.quit()

def test_checkout_sem_first_name():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "continue").click()
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "error-message-container"),
                "Error: First Name is required"
            )
        )
       
        mensagem = driver.find_element(
            By.CLASS_NAME, "error-message-container"
        ).text
        assert "Error: First Name is required" in mensagem
        assert "checkout-step-one.html" in driver.current_url
    finally:
        driver.quit()
def test_checkout_sem_last_name():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Ana")
        driver.find_element(By.ID, "continue").click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "error-message-container"),
                "Error: Last Name is required"
            )
        )
        mensagem = driver.find_element(
            By.CLASS_NAME, "error-message-container"
        ).text
        assert "Error: Last Name is required" in mensagem
        assert "checkout-step-one.html" in driver.current_url
    finally:
        driver.quit()