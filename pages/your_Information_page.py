import allure
from playwright.sync_api import expect

from locators.your_Information_page_locators import YourInformationPageLocators
from pages.base_page import BasePage


class YourInformationPage(BasePage):
    locators = YourInformationPageLocators()

    @allure.step('Проверка наличия элементов на странице информации о покупателе')
    def check_your_information_page(self):
        expect(self.page.locator(self.locators.FIRST_NAME_FIELD), 'Отсутствует или не видимо поле Имя').to_be_visible()
        expect(self.page.locator(self.locators.LAST_NAME_FIELD), 'Отсутствует или не видимо поле Фамилия').to_be_visible()
        expect(self.page.locator(self.locators.POST_CODE_FIELD), 'Отсутствует или не видимо поле Адрес').to_be_visible()
        expect(self.page.locator(self.locators.CANSEL_BUTTON), 'Отсутствует или не кнопка Отмены').to_be_visible()
        expect(self.page.locator(self.locators.CONTINUE_BUTTON), 'Отсутствует или не кнопка Продолжения').to_be_visible()