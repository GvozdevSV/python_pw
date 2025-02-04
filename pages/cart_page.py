import random

import allure

from locators.cart_page_locators import CartPageLocators
from pages.base_page import BasePage
from playwright.sync_api import expect


class CartPage(BasePage):
    locators = CartPageLocators()

    @allure.step('Проверка наличия элементов страницы корзина')
    def check_cart_page_elements(self):
        expect(self.page.locator(self.locators.PAGE_TITLE), 'Отсутствует заголовок страницы').to_have_text('Your Cart')
        expect(self.page.locator(self.locators.PRODUCT_TITLES).first, 'Отсутствует заголовок товара').to_be_visible()
        expect(self.page.locator(self.locators.DESCRIPTIONS).first, 'Отсутствует описание товара').to_be_visible()
        expect(self.page.locator(self.locators.PRISES).first, 'Отсутствует цена товара').to_be_visible()
        expect(self.page.locator(self.locators.REMOVE_BUTTONS).first,
               'Отсутствует кнопка удаления товара товара').to_be_visible()
        expect(self.page.locator(self.locators.CONTINUE_SHOPPING_BUTTON).first,
               'Отсутствует кнопка продолжить покупки').to_be_visible()
        expect(self.page.locator(self.locators.CHECKOUT_BUTTON).first, 'Отсутствует оформления покупки').to_be_visible()

    @allure.step('Получение значений товара из корзины')
    def get_product_values_from_cart_page(self):
        title = self.page.locator(self.locators.PRODUCT_TITLES).text_content()
        description = self.page.locator(self.locators.DESCRIPTIONS).text_content()
        prise = self.page.locator(self.locators.PRISES).text_content()
        return title, description, prise

    @allure.step('Получение имен товаров из корзины')
    def get_all_product_names_from_cart_page(self):
        return self.page.locator(self.locators.PRODUCT_TITLES).all_text_contents()

    @allure.step('Удаление случайного товара из козины')
    def delete_random_product(self):
        all_products = self.page.locator(self.locators.REMOVE_BUTTONS).all()
        random.choice(all_products).click()

    @allure.step('Нажатие кнопки Вернуться к покупкам')
    def press_continue_shopping_button(self):
        self.page.locator(self.locators.CONTINUE_SHOPPING_BUTTON).click()

    @allure.step('Нажатие кнопки Перейти к оформлению')
    def press_checkout_button(self):
        self.page.locator(self.locators.CHECKOUT_BUTTON).click()
