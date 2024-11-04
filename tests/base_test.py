
from playwright.sync_api import sync_playwright

from pages.base_page import BasePage
from pages.login_page import LoginPage


class BaseTest:
    browser = sync_playwright().start().chromium.launch(headless=False)
    page = browser.new_page()
    login_page = LoginPage(page)



