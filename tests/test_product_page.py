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
