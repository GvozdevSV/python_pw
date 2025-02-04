import time

import allure
import pytest

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

    testdata = [('standard_us', os.getenv('PASSWORD')),
                ('standard_user', os.getenv('PASSWORD')[:-1])]

    @allure.title('Авторизация с не корректным логином или паролем')
    @pytest.mark.parametrize("wrong_login, wrong_password", testdata)
    def test_wrong_password_or_login(self, browser_context, wrong_login, wrong_password):
        login_page = LoginPage(browser_context)
        login_page.simple_login(wrong_login, wrong_password)
        assert login_page.get_error() == 'Epic sadface: Username and password do not match any user in this service', \
            "Не появилось сообщение о не корректном логине и пароле"
