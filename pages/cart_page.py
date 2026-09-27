from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT = (By.ID, "checkout")

    def item_names(self):
        return [item.text for item in self.find_all(self.ITEM_NAMES)]

    def checkout(self):
        self.click(self.CHECKOUT)
