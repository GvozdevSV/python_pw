import time
from tests.base_test import BaseTest
import os
from dotenv import load_dotenv

load_dotenv()


class TestLoginPage(BaseTest):

    def test_login(self):
        self.login_page.go_to_login_page()
        self.login_page.fil_login_field('standard_user')
        self.login_page.fil_password_field(os.getenv('PASSWORD'))
        self.login_page.press_login_button()
        self.login_page.check_login()
