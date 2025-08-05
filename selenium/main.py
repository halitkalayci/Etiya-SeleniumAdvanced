import selenium
import selenium.webdriver
import time
# Eski bir versiyonla çalışıyor isek (WebDriver install etmeyen), bu satırları kullanabiliriz.
#from webdriver_manager.chrome import ChromeDriverManager
#driver = selenium.webdriver.Chrome(ChromeDriverManager().install())

driver = selenium.webdriver.Chrome()

driver.get("https://google.com")

username_input = driver.find_element()