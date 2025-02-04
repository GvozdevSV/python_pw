import allure
from playwright.sync_api import expect

from locators.overview_page_locators import OverviewPageLocators
from pages.base_page import BasePage


class OverviewPage(BasePage):
    locators = OverviewPageLocators()

    @allure.step('Проверка заголовков страницы Завершения покупки')
    def check_labels(self):
        assert (self.page.locator(self.locators.SUMMARY_INFO_LABEL).all_text_contents() ==
                ['Payment Information:', 'Shipping Information:', 'Price Total']), \
            "На странице завершения покупки есть не все заголовки"

    @allure.step('Проверка полей страницы Завершения покупки')
    def check_overview_page_fields(self):
        expect(self.page.locator(self.locators.TITLE), "Отсутствует заголовок страницы").to_have_text('Checkout: Overview')
        self.check_labels()
        expect(self.page.locator(self.locators.PAYMENT_VALUE), "Отсутствует название карты").to_contain_text('SauceCard')
        expect(self.page.locator(self.locators.SHIPPING_VALUE), "Отсутствует способ доставки").to_contain_text(
            'Free Pony Express Delivery!')
        expect(self.page.locator(self.locators.SUBTOTAL_LABEL), "Отсутствует подзаголовок").to_contain_text('Item total: $')
        expect(self.page.locator(self.locators.TAX_LABEL), "Отсутствует подзаголовок налог").to_contain_text('Tax: $')
        expect(self.page.locator(self.locators.TOTAL_LABEL), "Отсутствует подзаголовок Итого").to_contain_text('Total: $')
        expect(self.page.locator(self.locators.FINISH_BUTTON), "Отсутствует кнопка Закончить").to_be_visible()
        expect(self.page.locator(self.locators.CANSEL_BUTTON), "Отсутствует кнопка Отменить").to_be_visible()
