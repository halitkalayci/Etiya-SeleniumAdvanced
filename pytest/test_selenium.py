from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest 
@pytest.mark.parametrize("username,password", [("standard_user","secret_sauce")])
def test_login(username,password):
    #headless
    options = Options()
    options.add_argument(argument="--headless")

    driver = Chrome(options=options)
    driver.get("https://www.saucedemo.com/v1/index.html")
    wait = WebDriverWait(driver, 10)
    
    # magic-string
    username_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-test='username']")))
    username_input.send_keys(username)

    password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-test='password']")))
    password_input.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    assert driver.current_url == "https://www.saucedemo.com/v1/inventory.html"
    
def test_login_error():
    # Başarısız giriş yapıldığında error textini doğrulayalım.
    pass
