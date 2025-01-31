import allure
from playwright.sync_api import expect

from data.urls import Urls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    @allure.step('Переход на страницу')
    def go_to_login_page(self):
        self.page.goto(Urls.enter_url)

    @allure.step('Заполнение поля логин')
    def fil_login_field(self, login):
        self.page.get_by_placeholder(self.locators.LOGIN_FIELD).fill(login)

    @allure.step('Заполнение поля пароль')
    def fil_password_field(self, password):
        self.page.get_by_placeholder(self.locators.PASSWORD_FIELD).fill(password)

    @allure.step('Нажатие кнопки Login')
    def press_login_button(self):
        self.page.locator(self.locators.SUBMIT_BUTTON).click()

    @allure.step('Проверка авторизации')
    def check_login(self):
        expect(self.page.get_by_text('Sauce Labs Backpack'), "Пользователь не авторизовался").to_be_visible()

    @allure.step('Простая авторизация')
    def simple_login(self, login, password):
        self.page.goto(Urls.enter_url)
        self.page.get_by_placeholder(self.locators.LOGIN_FIELD).fill(login)
        self.page.get_by_placeholder(self.locators.PASSWORD_FIELD).fill(password)
        self.page.locator(self.locators.SUBMIT_BUTTON).click()

    @allure.step('Получение текста ошибки при авторизации')
    def get_error(self):
        return self.page.locator(self.locators.ERROR).text_content()

