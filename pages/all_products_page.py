import random
import time
from playwright.sync_api import expect
from locators.all_products_page_locators import AllProductsPageLocators
from pages.base_page import BasePage


class AllProductsPage(BasePage):
    locators = AllProductsPageLocators()

    def go_to_random_product(self):
        time.sleep(2)
        self.page.locator(self.locators.PRODUCT_TITLES).click()
