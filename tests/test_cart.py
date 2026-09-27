import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utils.test_data import BACKPACK, BIKE_LIGHT


@pytest.mark.smoke
def test_add_product_updates_cart_badge(logged_in):
    inventory = InventoryPage(logged_in)
    inventory.add_to_cart(BACKPACK)

    assert inventory.cart_count() == 1


@pytest.mark.regression
def test_remove_product_clears_cart_badge(logged_in):
    inventory = InventoryPage(logged_in)
    inventory.add_to_cart(BACKPACK)
    inventory.remove_from_cart(BACKPACK)

    assert inventory.cart_count() == 0


@pytest.mark.regression
def test_cart_lists_added_products(logged_in):
    inventory = InventoryPage(logged_in)
    inventory.add_to_cart(BACKPACK)
    inventory.add_to_cart(BIKE_LIGHT)
    inventory.open_cart()

    assert CartPage(logged_in).item_names() == [BACKPACK, BIKE_LIGHT]
