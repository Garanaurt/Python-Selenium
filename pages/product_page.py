from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import ProductPageLocators as PPL


class ProductPage(BasePage):
    def add_to_cart(self): #добавить товар в корзину
        add_butt = self.browser.find_element(*ProductPageLocators.BUTTON)
        add_butt.click()
        self.solve_quiz_and_get_code() #Запускаем код из base_page

    def is_element_added_in_cart(self): #проверка сообщения о добавлении в корзину
        assert self.is_element_present(*ProductPageLocators.ADDED_MESS), "Не добавлено"

    def is_name_added_product_valid(self): #Проверка имени продукта и имя добавленного в корзину
        assert self.name_product(
            *PPL.NAME_PRODUCT) == self.name_added_in_cart(*PPL.NAME_PR_ADD_BASK), "Имя продукта не ок"
        
    def is_price_added_prod_valid(self): #Проверка цены
        assert self.price_product(*PPL.PRICE_PRODUCT) == self.price_product(*PPL.FIRST_BUY_CART_PRICE), "Цена не ок"
        
    def should_not_be_success_message(self): #проверка что нет элемента с сообщением о добавлении в корзину
        assert self.is_not_element_present(*ProductPageLocators.ADDED_MESS), \
            "Сообщение о добавлении в корзину есть, но его сейчас быть не должно"
    
    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_MESS), "Элемент есть на странице и не пропадает"
        
    

