import selenium
import selenium.webdriver
import time
from selenium.webdriver.common.by import By
# Eski bir versiyonla çalışıyor isek (WebDriver install etmeyen), bu satırları kullanabiliriz.
#from webdriver_manager.chrome import ChromeDriverManager
#driver = selenium.webdriver.Chrome(ChromeDriverManager().install())

driver = selenium.webdriver.Chrome()

# Unable to locate hatası => 
# Ya sayfa yüklenmedi ?
# Ya da yüklensede beklediğim element yok ya da yanlış attr kullanıyorum?
def login_success():
    driver.get("https://www.saucedemo.com/v1/index.html")
    driver.maximize_window()

    time.sleep(3)

    username_input = driver.find_element(By.XPATH, "//*[@data-test='username']")
    username_input.send_keys("standard_user")

    password_input = driver.find_element(By.XPATH, "//*[@data-test='password']")
    password_input.send_keys("secret_sauce")

    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()

    time.sleep(5)

    print(driver.current_url == "https://www.saucedemo.com/v1/inventory.html")

def login_error_wrong_password():
    driver.get("https://www.saucedemo.com/v1/index.html")
    driver.maximize_window()

    time.sleep(3)

    username_input = driver.find_element(By.XPATH, "//*[@data-test='username']")
    username_input.send_keys("standard_user")

    password_input = driver.find_element(By.XPATH, "//*[@data-test='password']")
    password_input.send_keys("secret_sauce1")

    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()

login_success()
login_error_wrong_password()

time.sleep(5000)
