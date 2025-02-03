import allure

from pages.all_products_page import AllProductsPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage


@allure.suite('Карточка товара')
class TestProductPage:

    @allure.title('Проверка отображения карточки товара')
    def test_product_page_display(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.go_to_random_product()
        product_page = ProductPage(browser_context)
        product_page.check_product_card()

    @allure.title('Проверка добавления товара в корзину из карточки товара')
    def test_add_product_to_cart_from_product_page(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.go_to_random_product()
        product_page = ProductPage(browser_context)
        product_from_page = product_page.get_product_values_from_product_page()
        product_page.press_add_to_cart_button()
        assert product_page.get_cart_badge_value() == '1', "Количество товаров не отобразилось на иконке корзины"
        all_products_page.go_to_cart()
        cart_page = CartPage(browser_context)
        product_from_cart = cart_page.get_product_values_from_cart_page()
        assert product_from_page == product_from_cart, "В корзину не добавился или добавился не корректный товар"

    @allure.title('Проверка удаления товара из корзины со страницы карточки товара')
    def test_delete_product_from_product_page(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.add_first_and_last_product_to_cart()
        all_products_page.go_to_cart()
        cart_page = CartPage(browser_context)
        in_cart_before = cart_page.get_all_product_names_from_cart_page()
        in_badge_before = cart_page.get_cart_badge_value()
        cart_page.press_continue_shopping_button()
        all_products_page.go_to_product_cart_by_product_name(in_cart_before[0])
        product_page = ProductPage(browser_context)
        product_page.press_remove_product_button()
        in_badge_after = cart_page.get_cart_badge_value()
        all_products_page.go_to_cart()
        in_cart_after = cart_page.get_all_product_names_from_cart_page()
        assert in_cart_before[0] not in in_cart_after, "Товар не удалился из корзины"
        assert int(in_badge_after) == int(in_badge_before) - 1, "Количество товаров на бейдже не уменьшилось на один"
