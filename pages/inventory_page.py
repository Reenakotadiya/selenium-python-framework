from selenium.webdriver.common.by import By

from pages.base_page import BasePage


def _slug(product_name):
    return product_name.lower().replace(" ", "-")


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def title(self):
        return self.text_of(self.TITLE)

    def item_count(self):
        return len(self.find_all(self.ITEMS))

    def add_to_cart(self, product_name):
        self.click((By.CSS_SELECTOR, f"[data-test='add-to-cart-{_slug(product_name)}']"))

    def remove_from_cart(self, product_name):
        self.click((By.CSS_SELECTOR, f"[data-test='remove-{_slug(product_name)}']"))

    def cart_count(self):
        """Number shown on the cart badge (0 when the badge is hidden)."""
        badges = self.find_all(self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def open_cart(self):
        self.click(self.CART_LINK)
