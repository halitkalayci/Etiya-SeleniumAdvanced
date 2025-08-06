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

    error_container = driver.find_element(By.XPATH, "//*[@data-test='error']")

    if error_container.value_of_css_property("display") == "none":
        print("Element hiç gözükmedi.")
    if error_container.text != "Epic sadface: Username and password do not match any user in this service":
        print("Mesaj yanlış.")

def product_count_test():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    driver.maximize_window()

    inv_container = driver.find_element(By.ID, "inventory_container")

    inv_items = inv_container.find_elements(By.CLASS_NAME, "inventory_item")

    print(len(inv_items) == 6)


#login_success()
login_error_wrong_password()
#product_count_test()

time.sleep(5000)

# 1. test case => kilitli kullanıcı giriş testi -> Mesajın "Epic sadface: Sorry, this user has been locked out." olması
# 2. test case => username boş gönderilme testi -> Epic sadface: Username is required
# 3. test case => password boş gönderilme testi ->
# 4. test case -> Ana sayfada ürün sayısını bulan fonks.