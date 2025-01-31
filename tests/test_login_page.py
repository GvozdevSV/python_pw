import time

import allure
from pages.login_page import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()


@allure.suite('Авторизация')
class TestLoginPage:

    @allure.title('Корректная авторизация')
    def test_login(self, browser_context):
        login_page = LoginPage(browser_context)
        login_page.go_to_login_page()
        login_page.fil_login_field('standard_user')
        login_page.fil_password_field(os.getenv('PASSWORD'))
        login_page.press_login_button()
        login_page.check_login()
