import allure

from pages.all_products_page import AllProductsPage
from pages.cart_page import CartPage


@allure.suite('Страница все товары')
class TestAllProductsPage:

    @allure.title('Проверка отображения страницы все товары')
    def test_all_products_page_display(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.check_products_page()

    @allure.title('Проверка добавления двух товаров в корзину со страницы все товары')
    def test_add_two_products_from_all_products_page(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.add_first_and_last_product_to_cart()
        added_products_on_page = all_products_page.get_add_to_cart_products_name()
        all_products_page.go_to_cart()
        cart_page = CartPage(browser_context)
        added_products_on_cart = cart_page.get_all_product_names_from_cart_page()
        assert added_products_on_page == added_products_on_cart, "Добавленные товары не отобразились в корзине"
