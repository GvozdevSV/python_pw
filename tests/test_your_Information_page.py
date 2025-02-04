import allure

from pages.all_products_page import AllProductsPage
from pages.cart_page import CartPage
from pages.your_Information_page import YourInformationPage


@allure.suite('Информация о покупателе')
class TestYourInformationPage:

    @allure.title('Проверка отображения страницы Информация о покупателе')
    def test_your_information_page_display(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.go_to_cart()
        cart_page = CartPage(browser_context)
        cart_page.press_checkout_button()
        your_information_page = YourInformationPage(browser_context)
        your_information_page.check_your_information_page()

    @allure.title('Проверка заполнения полей страницы Информация о покупателе')
    def test_field_your_information_page(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.go_to_cart()
        cart_page = CartPage(browser_context)
        cart_page.press_checkout_button()
        your_information_page = YourInformationPage(browser_context)
        your_information_page.check_fill_your_information_fields()
