from playwright.async_api import Page
from playwright.sync_api import sync_playwright


class BasePage:
    def __init__(self, page):
        self.page = page

    @staticmethod
    def open(url, page: Page):
        return page.goto(url)

