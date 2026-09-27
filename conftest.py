import os
from pathlib import Path

import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from utils.test_data import BASE_URL, STANDARD_USER, PASSWORD

SCREENSHOT_DIR = Path("reports/screenshots")


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox"], help="Browser to run tests on")
    parser.addoption("--headless", action="store_true", help="Run browser without a visible window")


def _chrome(headless):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    # Stop Chrome's "password breach" popup from blocking the page after login.
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    return webdriver.Chrome(options=options)


def _firefox(headless):
    options = webdriver.FirefoxOptions()
    if headless:
        options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080)
    return driver


@pytest.fixture
def driver(request):
    """Fresh browser for every test. Selenium Manager downloads the driver automatically."""
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless") or os.getenv("CI") == "true"
    driver = _chrome(headless) if browser == "chrome" else _firefox(headless)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in(driver):
    """Browser already logged in as the standard user."""
    LoginPage(driver).open(BASE_URL).login(STANDARD_USER, PASSWORD)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Save a screenshot whenever a test fails."""
    outcome = yield
    report = outcome.get_result()
    driver = item.funcargs.get("driver")
    if report.when == "call" and report.failed and driver:
        SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
        driver.save_screenshot(str(SCREENSHOT_DIR / f"{item.name}.png"))
