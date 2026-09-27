# Selenium Python Automation Framework

[![UI Tests](https://github.com/Reenakotadiya/selenium-python-framework/actions/workflows/tests.yml/badge.svg)](https://github.com/Reenakotadiya/selenium-python-framework/actions/workflows/tests.yml)

A clean, maintainable **UI test automation framework** built with **Selenium 4, Python and Pytest**, using the **Page Object Model**.

It tests the demo e-commerce site [SauceDemo](https://www.saucedemo.com/): login, cart and full checkout.

---

## ✨ Features

- **Page Object Model**: locators and page actions live in `pages/`, and tests stay short and readable
- **Explicit waits**: no `time.sleep()`, so tests are stable and fast
- **Data-driven tests**: negative login cases run with `pytest.mark.parametrize`
- **Cross-browser**: Chrome or Firefox, with an optional headless mode
- **Automatic driver setup**: Selenium Manager downloads the right driver, with no manual installs
- **Screenshots on failure**: saved to `reports/screenshots/`
- **HTML report**: generated after every run at `reports/report.html`
- **CI/CD**: tests run automatically on GitHub Actions for every push

---

## 📁 Project Structure

```
selenium-python-framework/
├── pages/                  # Page Object classes
│   ├── base_page.py        # Shared actions with explicit waits
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                  # Test cases
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
├── utils/
│   └── test_data.py        # URLs, users and test data
├── conftest.py             # Browser fixtures, options, screenshot hook
├── pytest.ini              # Pytest settings, markers and HTML report
├── requirements.txt
└── .github/workflows/      # GitHub Actions pipeline
```

---

## 🧪 Test Coverage

| Area | Scenario | Type |
|---|---|---|
| Login | Valid login opens the Products page | Smoke |
| Login | Locked user, wrong password, empty username, empty password | Regression |
| Cart | Adding a product updates the cart badge | Smoke |
| Cart | Removing a product clears the cart badge | Regression |
| Cart | Cart lists all added products | Regression |
| Checkout | Complete order end to end | Smoke |
| Checkout | First name is required | Regression |

---

## 🚀 How to Run

**1. Clone and install**

```bash
git clone https://github.com/Reenakotadiya/selenium-python-framework.git
cd selenium-python-framework
pip install -r requirements.txt
```

**2. Run tests**

```bash
pytest                          # all tests in Chrome
pytest -m smoke                 # only smoke tests
pytest -m regression            # only regression tests
pytest --browser firefox        # run in Firefox
pytest --headless               # run without opening a browser window
```

**3. View the report**

Open `reports/report.html` in your browser.

---

## 🛠️ Tech Stack

Python · Selenium 4 · Pytest · pytest-html · GitHub Actions

---

## 👩‍💻 Author

**Reena Kotadiya**, QA Automation Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Reena%20Kotadiya-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/reena-kotadiya-1a7073170)

💼 Available for freelance test automation projects.
