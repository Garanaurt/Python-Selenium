from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME, "login_form")
    REGISTRATION_FORM = (By.CLASS_NAME, "register_form")

class ProductPageLocators():
    BUTTON = (By.CLASS_NAME, "btn-add-to-basket") #добавление в корзину
    ADDED_MESS = (By.CSS_SELECTOR, "div.alert:first-child .alertinner") #сообщение о том что продукт добавлен
    NAME_PR_ADD_BASK = (By.CSS_SELECTOR, "div.alert:first-child .alertinner strong") #имя добавленного в корзину
    NAME_PRODUCT = (By.CLASS_NAME, "product_main h1") #название продукта
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main  .price_color") #цена 
    FIRST_BUY_CART_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong") #цена в корзине

