# Web sitesindeki imageların doğru yüklenip yüklenmediğini test etmek.

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import requests

driver = Chrome()

driver.get("https://the-internet.herokuapp.com/broken_images")

images = driver.find_elements(By.TAG_NAME, "img")
print(len(images))

content_div = driver.find_element(By.ID, "content")
content_images = content_div.find_elements(By.TAG_NAME, "img")
print(len(content_images))

broken_imgs = []
for image in images:
    image_url = image.get_attribute("src")
    print(image_url)
    response = requests.get(image_url)
    if response.status_code != 200:
        broken_imgs.append(image_url)
print(f"Bozuk Imglar: {broken_imgs}")