import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from utils.test_data import BACKPACK, CUSTOMER


def _go_to_checkout(driver):
    inventory = InventoryPage(driver)
    inventory.add_to_cart(BACKPACK)
    inventory.open_cart()
    CartPage(driver).checkout()
    return CheckoutPage(driver)


@pytest.mark.smoke
def test_complete_order_end_to_end(logged_in):
    checkout = _go_to_checkout(logged_in)
    checkout.fill_details(**CUSTOMER)
    checkout.finish()

    assert checkout.confirmation_message() == "Thank you for your order!"


@pytest.mark.regression
def test_checkout_requires_first_name(logged_in):
    checkout = _go_to_checkout(logged_in)
    checkout.fill_details(first_name="", last_name=CUSTOMER["last_name"], postal_code=CUSTOMER["postal_code"])

    assert "First Name is required" in checkout.error_message()
