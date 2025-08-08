# basit-hızlı deneme dosyası

from selenium.webdriver import Chrome,Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver = Firefox()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dropdown")

# Eğer yukarıdaki HTML bu sayfaya ait değilse, sen kendi lokalde html dosyasını host edebilirsin.

# 2. Dropdown elementini bekle ve bul
dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dropdown"))
)

# 3. Dropdown'u seç ve Option 2'yi seç
select = Select(dropdown)
select.select_by_visible_text("Option 2")

# 4. Seçili değeri kontrol et
selected_option = select.first_selected_option
assert selected_option.text == "Option 2"


#frame_elem = driver.find_element(By.ID, "mce_0_ifr")
#driver.switch_to.frame(frame_elem)
#content = driver.find_element(By.XPATH, "//*[@id='tinymce']/p")
#driver.switch_to.parent_frame()
#sleep(2)
#content.clear()
#content.send_keys("Merhaba")
#sleep(50)