from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_login():
    driver = Chrome()
    driver.get("https://www.saucedemo.com/v1/index.html")
    wait = WebDriverWait(driver, 10)
    
    username_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-test='username']")))
    username_input.send_keys("standard_user")

    password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-test='password']")))
    password_input.send_keys("secret_sauce")

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    assert driver.current_url == "https://www.saucedemo.com/v1/inventory.html"
    
