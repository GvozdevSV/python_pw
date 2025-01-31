import allure

from pages.all_products_page import AllProductsPage


@allure.suite('Страница все товары')
class TestAllProductsPage:

    @allure.title('Проверка отображения страницы все товары')
    def test_all_products_page_display(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.check_products_page()
