import allure
from playwright.sync_api import Page


class BasePage:

    BADGE_VALUE = 'span[class="shopping_cart_badge"]'

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Переход на url')
    def open(self, url):
        return self.page.goto(url)

    @allure.step('Получение количества товаров отображенных на иконке корзины')
    def get_cart_badge_value(self):
        return self.page.locator(self.BADGE_VALUE).text_content()