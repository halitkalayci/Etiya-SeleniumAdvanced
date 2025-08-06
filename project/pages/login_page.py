# Sayfanın Yeteneklerinin Kodlanması.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Sayfadaki içerik tanımları?
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//*[@data-test='error']")
    
    def load(self):
        self.driver.get("https://www.saucedemo.com/v1/index.html")
        self.wait.until(EC.visibility_of_element_located(self.username_input))

    def login(self, username, password):
        self.wait.until(EC.element_to_be_clickable(self.username_input)).send_keys(username)
        self.wait.until(EC.element_to_be_clickable(self.password_input)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_message)).text