from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    ITEM_NAMES = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    CHECKOUT = (By.ID, "checkout")

    def item_names(self):
        self.find(self.CHECKOUT)  # wait until the cart page has actually loaded
        return [item.text for item in self.find_all(self.ITEM_NAMES)]

    def checkout(self):
        self.click(self.CHECKOUT)
