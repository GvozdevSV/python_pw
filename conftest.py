import os

import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

from pages.login_page import LoginPage

load_dotenv()

@pytest.fixture()
def page():
    if os.getenv('CI') == 'local':
        browser = sync_playwright().start().chromium.launch(headless=False)
        page = browser.new_context(viewport={'width': 1920, 'height': 1080}).new_page()
        yield page
        page.close()
    if os.getenv('CI') == 'cloud':
        browser = sync_playwright().start().chromium.launch(headless=True)
        page = browser.new_context(viewport={'width': 1920, 'height': 1080}).new_page()
        yield page
        page.close()
        page.

@pytest.fixture()
def login(page):
    login_page = LoginPage(page)
    login_page.go_to_login_page()
    login_page.fil_login_field('standard_user')
    login_page.fil_password_field(os.getenv('PASSWORD'))
    login_page.press_login_button()
    return login

