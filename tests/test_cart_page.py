import allure

from pages.all_products_page import AllProductsPage
from pages.cart_page import CartPage


@allure.suite('Корзина')
class TestCartPage:

    @allure.title('Проверка отображения страницы Корзина')
    def test_check_cart_page(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.add_random_product_to_cart()
        all_products_page.go_to_cart()
        cart_page = CartPage(browser_context)
        cart_page.check_cart_page_elements()
