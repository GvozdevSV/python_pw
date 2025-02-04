import allure
from playwright.sync_api import expect

from locators.your_Information_page_locators import YourInformationPageLocators
from pages.base_page import BasePage
from generator.generator import generated_your_information


class YourInformationPage(BasePage):
    locators = YourInformationPageLocators()

    @allure.step('Проверка наличия элементов на странице информации о покупателе')
    def check_your_information_page(self):
        expect(self.page.locator(self.locators.FIRST_NAME_FIELD), 'Отсутствует или не видимо поле Имя').to_be_visible()
        expect(self.page.locator(self.locators.LAST_NAME_FIELD), 'Отсутствует или не видимо поле Фамилия').to_be_visible()
        expect(self.page.locator(self.locators.POST_CODE_FIELD), 'Отсутствует или не видимо поле Адрес').to_be_visible()
        expect(self.page.locator(self.locators.CANSEL_BUTTON), 'Отсутствует или не кнопка Отмены').to_be_visible()
        expect(self.page.locator(self.locators.CONTINUE_BUTTON), 'Отсутствует или не кнопка Продолжения').to_be_visible()

    @allure.step('Получение текста ошибки')
    def get_error(self):
        return self.page.locator(self.locators.ERROR).text_content()

    @allure.step('Заполнение полей информации о покупателе')
    def fill_your_information_fields(self, first_name, last_name, post_code):
        self.page.locator(self.locators.FIRST_NAME_FIELD).clear()
        self.page.locator(self.locators.FIRST_NAME_FIELD).fill(first_name)
        self.page.locator(self.locators.LAST_NAME_FIELD).clear()
        self.page.locator(self.locators.LAST_NAME_FIELD).fill(last_name)
        self.page.locator(self.locators.POST_CODE_FIELD).clear()
        self.page.locator(self.locators.POST_CODE_FIELD).fill(post_code)
        self.page.locator(self.locators.CONTINUE_BUTTON).click()

    @allure.step('Проверка вариантов заполнения полей информации о покупателе')
    def check_fill_your_information_fields(self):
        your_information = next(generated_your_information())
        # Пустое поле Имя
        self.fill_your_information_fields(
            '',
            your_information.last_name,
            your_information.post_code
        )
        assert self.get_error() == 'Error: First Name is required', "Не появилось сообщение о пустом поле Имя"
        # Пустое поле Фамилия
        self.fill_your_information_fields(
            your_information.first_name,
            '',
            your_information.post_code
        )
        assert self.get_error() == 'Error: Last Name is required', "Не появилось сообщение о пустом поле Фамилия"
        # Пустое поле Почтовый код
        self.fill_your_information_fields(
            your_information.first_name,
            your_information.last_name,
            ''
        )
        assert self.get_error() == 'Error: Postal Code is required', "Не появилось сообщение о пустом поле Почтовый код"
        # Все поля заполнены
        self.fill_your_information_fields(
            your_information.first_name,
            your_information.last_name,
            your_information.post_code
        )
        expect(self.page.locator(self.locators.TITLE), "Не произошел переход на страницу подтверждения заказа"
               ).to_have_text('Checkout: Overview')
