from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait # Element bulma işlemine wait işlemini entegre eder.
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
# wait kütüphaneleri-kodları

driver = Chrome() 
driver.maximize_window()
driver.get("https://www.saucedemo.com/v1/index.html")

# Explicit Wait
# Belirli bir koşulun gerçekleşmesini *maksimum* süre boyunca bekler, koşul sağlanır sağlanmaz bekleme sona erer.
wait = WebDriverWait(driver, 10)
username_input = wait.until(
    expected_conditions.visibility_of_element_located((By.XPATH, "//*[@data-test='username']"))
)
username_input.send_keys("standard_user")

# presence_of_element_located -> Element DOM'da var mı?
# visibility_of_element_located -> Element DOMda var ve görünür mü?
# element_to_be_clickable -> Element domda var, görünür ve tıklanabilir?
# text_to_be_present_in_element -> Belirli bir yazı geldi mi (elementin içinde)?
# alert_is_present -> Alert penceresi açıldı mı?

# Fluent Wait


sleep(5000)