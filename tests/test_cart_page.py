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

    @allure.title('Удаление товара из корзины')
    def test_delete_product_from_cart(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.add_first_and_last_product_to_cart()
        all_products_page.go_to_cart()
        cart_page = CartPage(browser_context)
        in_cart_before = cart_page.get_all_product_names_from_cart_page()
        in_badge_before = cart_page.get_cart_badge_value()
        cart_page.delete_random_product()
        in_cart_after = cart_page.get_all_product_names_from_cart_page()
        in_badge_after = cart_page.get_cart_badge_value()
        assert in_cart_after != in_cart_before, "Количество товаров в корзине не изменилось"
        assert int(in_badge_after) == int(in_badge_before) - 1, "Количество товаров на бейдже не уменьшилось на один"

