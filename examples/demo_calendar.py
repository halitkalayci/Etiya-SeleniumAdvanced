from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import random

link = "https://uxsolutions.github.io/bootstrap-datepicker/?markup=input&format=&weekStart=&startDate=&endDate=&startView=0&minViewMode=0&maxViewMode=4&todayBtn=false&clearBtn=false&language=en&orientation=auto&multidate=&multidateSeparator=&keyboardNavigation=on&forceParse=on#sandbox"

driver = Chrome()
driver.get(link)
driver.maximize_window()

time.sleep(1)

calendar = driver.find_element(By.XPATH, "//*[@id='sandbox-container']/input")
calendar.click()
time.sleep(1)
days = driver.find_elements(By.CSS_SELECTOR, "td.day:not(.old):not(.new)")
random_day = random.choice(days)
random_day.click()
time.sleep(300)