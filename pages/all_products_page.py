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

    @allure.step('Проверка наличия элементов страницы все товары')
    def check_products_page(self):
        expect(self.page.locator(self.locators.PAGE_TITLE), 'Отсутствует заголовок страницы').to_have_text('Products')
        all_products_titles = self.page.locator(self.locators.PRODUCT_TITLES).all()
        assert len(all_products_titles) > 1, "На странице меньше двух заголовков товаров"
        all_products_images = self.page.locator(self.locators.IMAGES).all()
        assert len(all_products_images) > 1, "На странице меньше двух фотографий товаров"
        all_products_description = self.page.locator(self.locators.DESCRIPTIONS).all()
        assert len(all_products_description) > 1, "На странице меньше двух описаний товаров"
        all_products_prises = self.page.locator(self.locators.PRISES).all()
        assert len(all_products_prises) > 1, "На странице меньше двух цен товаров"
        all_to_cart_buttons = self.page.locator(self.locators.ADD_TO_CART_BUTTONS).all()
        assert len(all_to_cart_buttons) > 1, "На странице меньше двух кнопок добавления товаров в корзину"
        expect(self.page.locator(self.locators.CART_ICON), 'Отсутствует иконка корзины').to_be_visible()
