from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        #
        self.sort_dropdown = (By.XPATH, "//*[@id='inventory_filter_container']/select")
        #
    def load(self):
        # Eğer giriş yapma zorunluluğu olan bir sayfa ise? Diğer sayfalarla entegre çalışabilir.
        self.driver.get("https://www.saucedemo.com/v1/inventory.html")
        self.wait.until(EC.visibility_of_element_located(self.sort_dropdown))

    def change_sort(self):
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_value("za")

# POM mimarisine uygun inventory pagede kendi belirlediğimiz 3 farklı test case'i yazalım.