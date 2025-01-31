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


