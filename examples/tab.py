from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
driver = Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(3)

click_here = driver.find_element(By.XPATH, "//*[@id='content']/div/a")
click_here.click()


time.sleep(3)
#
windows = driver.window_handles #Tüm sekmeleri al
driver.switch_to.window(windows[1]) # Tüm sekmeler içindeki X'inci (1) indexe git
#
h3 = driver.find_element(By.XPATH, "/html/body/div/h3")
print(h3.text)
time.sleep(500)