from playwright.sync_api import expect

from data.urls import Urls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def go_to_login_page(self):
        self.page.goto(Urls.enter_url)

    def fil_login_field(self, login):
        self.page.get_by_placeholder(self.locators.LOGIN_FIELD).fill(login)

    def fil_password_field(self, password):
        self.page.get_by_placeholder(self.locators.PASSWORD_FIELD).fill(password)

    def press_login_button(self):
        self.page.locator(self.locators.SUBMIT_BUTTON).click()

    def check_login(self):
        expect(self.page.get_by_text('Sauce Labs Backpack')).to_be_visible()
