from pages.inventory_page import InventoryPage

def test_za_sort(driver):
    page = InventoryPage(driver)
    page.load()
    page.change_sort()

# 