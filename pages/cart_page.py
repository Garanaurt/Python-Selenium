# страница корзины
from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def should_be_element_in_cart(self): # есть ли сообщение о том что корзина пустая
        basket_text = self.browser.find_element(*CartPageLocators.EMPTY_MESSAGE).text
        #print(basket_text) #для проверки
        assert "Your basket is empty." in basket_text, "Корзина не пустая"

    