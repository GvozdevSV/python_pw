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

    @allure.title('Удаление товаров со страницы Все товары')
    def test_delete_product_from_all_product_page(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.add_first_and_last_product_to_cart()
        all_products_page.go_to_cart()
        cart_page = CartPage(browser_context)
        in_cart_before = cart_page.get_all_product_names_from_cart_page()
        in_badge_before = cart_page.get_cart_badge_value()
        cart_page.press_continue_shopping_button()
        in_all_products_page_before = all_products_page.get_add_to_cart_products_name()
        all_products_page.delete_product_from_all_product_page_by_index(0)
        in_all_products_page_after = all_products_page.get_add_to_cart_products_name()
        all_products_page.go_to_cart()
        in_cart_after = cart_page.get_all_product_names_from_cart_page()
        in_badge_after = cart_page.get_cart_badge_value()
        assert in_cart_before == in_all_products_page_before, \
            "На странице все товары отображаются не все выбранные в корзину товары"
        assert in_cart_after == in_all_products_page_after, "В корзине не отображается товар оставшийся после удаления"
        assert in_cart_after != in_cart_before, "Количество товаров в корзине не изменилось"
        assert int(in_badge_after) == int(in_badge_before) - 1, "Количество товаров на бейдже не уменьшилось на один"

    @allure.title('Содержание дропдауна фильтрации страницы все товары')
    def test_product_filtering_dropdown_content(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.check_filter_dropdown()

    @allure.title('Фильтрация товаров по имени')
    def test_filter_products_by_name(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.check_filter_products_by_name()

