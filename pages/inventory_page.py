class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()

    def go_to_cart(self):
        self.driver.find_element("class name", "shopping_cart_link").click()