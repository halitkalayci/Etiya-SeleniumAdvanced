from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import random


driver = Chrome()
driver.maximize_window()
driver.get("https://patrickhlauke.github.io/recaptcha/")
time.sleep(3)
iframe_captcha = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/iframe")

driver.switch_to.frame(iframe_captcha)
click_span = driver.find_element(By.ID, "recaptcha-anchor")
click_span.click()

time.sleep(5000)