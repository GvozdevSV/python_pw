import os

import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

from pages.login_page import LoginPage

load_dotenv()


@pytest.fixture()
def browser_context():
    with sync_playwright() as p:
        if os.getenv('CI') == 'local':
            browser = p.chromium.launch(headless=False)
        if os.getenv('CI') == 'cloud':
            browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080}).new_page()
        yield context
        context.close()
        browser.close()


@pytest.fixture()
def login(browser_context):
    login_page = LoginPage(browser_context)
    login_page.go_to_login_page()
    login_page.fil_login_field('standard_user')
    login_page.fil_password_field(os.getenv('PASSWORD'))
    login_page.press_login_button()
