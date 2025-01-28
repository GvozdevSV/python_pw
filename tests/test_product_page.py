import time

from pages.all_products_page import AllProductsPage


class TestProductPage:

    def test_product_page_display(self, login, page):
        all_products_page = AllProductsPage(page)
        all_products_page.go_to_random_product()

        time.sleep(4)