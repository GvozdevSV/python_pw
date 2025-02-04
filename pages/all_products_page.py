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

    @allure.step('Добавление случайного товара в корзину')
    def add_random_product_to_cart(self):
        all_to_cart_buttons = self.page.locator(self.locators.ADD_TO_CART_BUTTONS).all()
        random.choice(all_to_cart_buttons).click()

    @allure.step('Переход в корзину')
    def go_to_cart(self):
        self.page.locator(self.locators.CART_ICON).click()

    @allure.step('Добавление первого и последнего товара в корзину')
    def add_first_and_last_product_to_cart(self):
        self.page.locator(self.locators.ADD_TO_CART_BUTTONS).first.click()
        assert self.get_cart_badge_value() == '1', "Добавление первого товара не отобразилось на иконке корзины"
        self.page.locator(self.locators.ADD_TO_CART_BUTTONS).last.click()
        assert self.get_cart_badge_value() == '2', "Добавление второго товара не отобразилось на иконке корзины"

    @allure.step('Получение имен товаров добавленных в корзину')
    def get_add_to_cart_products_name(self):
        return self.page.locator(self.locators.ADDED_PRODUCTS_NAME).all_text_contents()

    @allure.step('Удаление товара по индексу')
    def delete_product_from_all_product_page_by_index(self, index):
        self.page.locator(self.locators.REMOVE_BUTTONS).nth(index).click()

    @allure.step('Переход в карточку товара по названию товара')
    def go_to_product_cart_by_product_name(self, product_name):
        self.page.locator(self.locators.PRODUCT_TITLES).get_by_text(product_name).click()

    @allure.step('Получение всех отображаемых в корзине полей выбранных товаров')
    def get_add_to_cart_products_fields(self):
        names = self.page.locator(self.locators.ADDED_PRODUCTS_NAME).all_text_contents()
        descriptions = self.page.locator(self.locators.ADDED_PRODUCTS_DESCRIPTION).all_text_contents()
        prises = self.page.locator(self.locators.ADDED_PRODUCTS_PRISES).all_text_contents()
        return names, descriptions, prises

