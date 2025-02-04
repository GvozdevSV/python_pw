

class AllProductsPageLocators:
    PAGE_TITLE = 'span[class="title"]'
    PRODUCT_TITLES = 'div[data-test="inventory-item-name"]'
    IMAGES = '//img[@class="inventory_item_img"]'
    DESCRIPTIONS = '//div[@data-test="inventory-item-desc"]'
    PRISES = 'div[class="inventory_item_price"]'
    ADD_TO_CART_BUTTONS = 'button[class="btn btn_primary btn_small btn_inventory "]'
    CART_ICON = 'div[class="shopping_cart_container"]'
    ADDED_PRODUCTS_NAME = '//button[@class="btn btn_secondary btn_small btn_inventory "]//ancestor::div[@class="inventory_item"]//div[@class="inventory_item_name "]'
    ADDED_PRODUCTS_DESCRIPTION = '//button[@class="btn btn_secondary btn_small btn_inventory "]//ancestor::div[@class="inventory_item"]//div[@class="inventory_item_desc"]'
    ADDED_PRODUCTS_PRISES = '//button[@class="btn btn_secondary btn_small btn_inventory "]//ancestor::div[@class="inventory_item"]//div[@class="inventory_item_price"]'
    REMOVE_BUTTONS = 'button[class="btn btn_secondary btn_small btn_inventory "]'
    SELECT_FILTER = 'span[class="select_container"]'
    FILTER_ITEMS = 'option[value]'
