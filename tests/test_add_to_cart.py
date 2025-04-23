from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.load()
    login.login("standard_user", "secret_sauce")
    inventory.add_to_cart()
    inventory.go_to_cart()
    assert "cart" in driver.current_url