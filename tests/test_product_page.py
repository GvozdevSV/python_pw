import allure

from pages.all_products_page import AllProductsPage
from pages.product_page import ProductPage


@allure.suite('Карточка товара')
class TestProductPage:

    @allure.title('Проверка отображения карточки товара')
    def test_product_page_display(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.go_to_random_product()
        product_page = ProductPage(browser_context)
        product_page.check_product_card()
