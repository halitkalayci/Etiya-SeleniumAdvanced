# basit-hızlı deneme dosyası

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/v1/index.html")

sleep(1)
driver.execute_script("prompt('Adınızı Giriniz')")
sleep(1)
alert = driver.switch_to.alert # switch_to => focus websitesinin kendisinde iken, bunu alerte aktarır.
sleep(2)
print(alert.text)
alert.send_keys("Halit")
sleep(2)
alert.accept()
sleep(30)
