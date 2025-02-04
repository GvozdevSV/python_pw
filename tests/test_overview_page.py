
import allure

from pages.all_products_page import AllProductsPage
from pages.cart_page import CartPage
from pages.overview_page import OverviewPage
from pages.your_Information_page import YourInformationPage


@allure.suite('Страница завершения покупки')
class TestOverviewPage:

    @allure.title('Проверка отображения страницы Информация о покупателе')
    def test_displaying_overview_page_with_no_products(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.go_to_cart()
        cart_page = CartPage(browser_context)
        cart_page.press_checkout_button()
        your_information_page = YourInformationPage(browser_context)
        your_information_page.fill_your_information_fields(
            'Имя',
            'Фамилия',
            '1234'
        )
        overview_page = OverviewPage(browser_context)
        overview_page.check_overview_page_fields()

    @allure.title('Проверка корректности расчета суммы всех товаров')
    def test_correct_summ_on_overview_page(self, login, browser_context):
        all_products_page = AllProductsPage(browser_context)
        all_products_page.add_first_and_last_product_to_cart()
        all_products_page.go_to_cart()
        cart_page = CartPage(browser_context)
        prises_in_cart = cart_page.get_all_product_prises()
        cart_page.press_checkout_button()
        your_information_page = YourInformationPage(browser_context)
        your_information_page.fill_your_information_fields(
            'Имя',
            'Фамилия',
            '1234'
        )
        overview_page = OverviewPage(browser_context)
        prises_in_overview = overview_page.get_item_total_prise()
        assert sum(prises_in_cart) == prises_in_overview, "Сумма товаров расчитывается не корректно"
