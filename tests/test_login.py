import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.test_data import BASE_URL, LOCKED_USER, PASSWORD, STANDARD_USER


@pytest.mark.smoke
def test_valid_login_opens_products_page(driver):
    LoginPage(driver).open(BASE_URL).login(STANDARD_USER, PASSWORD)

    inventory = InventoryPage(driver)
    assert inventory.title() == "Products"
    assert inventory.item_count() > 0


@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (LOCKED_USER, PASSWORD, "Sorry, this user has been locked out"),
        (STANDARD_USER, "wrong_password", "Username and password do not match"),
        ("", PASSWORD, "Username is required"),
        (STANDARD_USER, "", "Password is required"),
    ],
    ids=["locked_user", "wrong_password", "empty_username", "empty_password"],
)
def test_invalid_login_shows_error(driver, username, password, expected_error):
    login = LoginPage(driver).open(BASE_URL)
    login.login(username, password)

    assert expected_error in login.error_message()
