
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()

class BaseTest:
    if os.getenv('CI') == 'local':
        browser = sync_playwright().start().chromium.launch(headless=False)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    if os.getenv('CI') == 'cloud':
        browser = sync_playwright().start().chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})

    login_page = LoginPage(page)



