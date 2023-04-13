from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #переход на логин
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") #тест
    CART_BTN = (By.CSS_SELECTOR, ".basket-mini a.btn-default") #переход в корзину
    REGISTR_OK_IMG = (By.CLASS_NAME, "icon-ok-sign") #иконка сообщения о успешной регистрации
    PRODUCT_LINK = (By.CSS_SELECTOR, ".col-sm-9 h3") #ссылка на первый продукт на главной странице

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME, "login_form")
    REGISTRATION_FORM = (By.CLASS_NAME, "register_form")
    REG_MAIL_FORM = (By.ID, "id_registration-email")
    REG_PASS_FORM = (By.ID, "id_registration-password1")
    REG_PASS_FORM_2 = (By.ID, "id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-primary")
    LOGOUT_BUTTON = (By.ID, "logout_link")

class ProductPageLocators():
    BUTTON = (By.CLASS_NAME, "btn-add-to-basket") #добавление в корзину
    ADDED_MESS = (By.CSS_SELECTOR, "div.alert:first-child .alertinner") #сообщение о том что продукт добавлен
    NAME_PR_ADD_BASK = (By.CSS_SELECTOR, "div.alert:first-child .alertinner strong") #имя добавленного в корзину
    NAME_PRODUCT = (By.CLASS_NAME, "product_main h1") #название продукта
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main  .price_color") #цена 
    FIRST_BUY_CART_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong") #цена в корзине
    

class CartPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "div p") #сообщение в корзине, проверка по тексту элемента позволяет знать пустая корзина или нет

