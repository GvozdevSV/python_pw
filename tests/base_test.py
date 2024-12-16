
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


class BaseTest:
    browser = sync_playwright().start().chromium.launch(headless=False)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    login_page = LoginPage(page)



