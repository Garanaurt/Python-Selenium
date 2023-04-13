from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
from .login_page import LoginPage


class MainPage(BasePage): 
    def should_not_be_success_message_on_main_page(self):
         #проверка что нет элемента с сообщением о добавлении в корзину на главной странице
        assert self.is_not_element_present(*ProductPageLocators.ADDED_MESS), \
            "Сообщение о добавлении в корзину на главной странице есть, но его сейчас быть не должно"


    