import random

import allure
from playwright.sync_api import expect
from locators.all_products_page_locators import AllProductsPageLocators
from pages.base_page import BasePage


class AllProductsPage(BasePage):
    locators = AllProductsPageLocators()

    @allure.step('Переход на случайную карточку товара')
    def go_to_random_product(self):
        all_products = self.page.locator(self.locators.PRODUCT_TITLES).all()
        random.choice(all_products).click()

