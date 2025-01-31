import allure

from locators.product_page_locators import ProductPageLocators
from pages.base_page import BasePage
from playwright.sync_api import expect


class ProductPage(BasePage):
    locators = ProductPageLocators()

    @allure.step('Проверка наличия элементов в карточке товара')
    def check_product_card(self):
        expect(self.page.locator(self.locators.TITLE), 'Отсутствует или не видим заголовок товара').to_be_visible()
        expect(self.page.locator(self.locators.IMAGE), 'Отсутствует или не видимо фото товара').to_be_visible()
        expect(self.page.locator(self.locators.DESCRIPTION),'Отсутствует или не видимо описание товара').to_be_visible()
        expect(self.page.locator(self.locators.PRISE), 'Отсутствует или не видна цена товара').to_be_visible()
        expect(self.page.locator(self.locators.ADD_TO_CART_BUTTON),
               'Отсутствует или не видна кнопка добавления товара в корзину').to_be_visible()
        expect(self.page.locator(self.locators.BACK_TO_PRODUCT_BUTTON),
               'Отсутствует или не видна кнопка возвращения к странице все товары').to_be_visible()
