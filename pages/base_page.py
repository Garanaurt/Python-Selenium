from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, LoginPageLocators
import math

class BasePage():
    def __init__(self, browser, url, timeout=10): #запуск и ожидание
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def should_be_cart_link(self): #есть ли страница корзины
        assert self.is_element_present(*BasePageLocators.CART_BTN), "Cart button is not presented"


    def go_to_cart(self): #переход на страницу корзины
        button = self.browser.find_element(*BasePageLocators.CART_BTN)
        button.click()


    def go_to_login_page(self): #переход на страницу логин
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()  


    def go_to_product_page(self): #переход на страницу продукта
        product_link = self.browser.find_element(*BasePageLocators.PRODUCT_LINK)
        product_link.click()


    def should_be_login_link(self): # есть ли кнопка перехода на логин
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
    

    def is_element_present(self, how, what): #проверка есть ли на странице элемент
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True


    def open(self): #переходим по ссылке
        self.browser.get(self.url)


    def solve_quiz_and_get_code(self):#из алерта получаем значение, считаем, отправляем, получаем код
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def name_added_in_cart(self, how, what):  #имя продукта добавленного в корзину
        name_elem = self.browser.find_element(how, what)
        name_text = name_elem.text
        #print(f'name in cart:{name_text}')# для проверки
        return name_text


    def name_product(self, how, what):   #имя продукта на странице
        name_elem = self.browser.find_element(how, what)
        name_text = name_elem.text
        #print(f'name:{name_text}') #для проверки
        return name_text
    

    def price_product(self, how, what): #цена продукта
        price_elem = self.browser.find_element(how, what)
        price = price_elem.text
        #print(price) #для проверки
        return price
    

    def is_not_element_present(self, how, what, timeout=4): # проверка есть элемент или нет и ожидание его появления 
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True # не дождался выпала ошибка
        return False # если дождался появления
    

    def is_disappeared(self, how, what, timeout=4): #элемент есть и мы ждем что он пропадёт в течении timeout
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False # False если элемент не исчез
        return True # True если элемент исчез за это время
    

    def mail_add_to_reg_form(self, how, what, mail): #заполняем мейл при регистрации
        mail_input = self.browser.find_element(how, what)
        mail_input.send_keys(mail)

    def password_add_to_form(self, how, what, password): #заполняем пасс при регистрации
        passw_input = self.browser.find_element(how, what)
        passw_input.send_keys(password)    

    def passw2_add_to_reg_form(self, how, what, password): #заполняем пасс при регистрации
        passw_input = self.browser.find_element(how, what)
        passw_input.send_keys(password)

    def registration_button(self, how, what): #кнопка регистрации
        button = self.browser.find_element(how, what)
        button.click()


    def is_registration_complete(self): #проверка сообщения об успешной регистрации
        assert self.is_element_present(*BasePageLocators.REGISTR_OK_IMG), "Регистрация не успешна"


    def is_user_autorized(self): #проверка залогинен юзер или нет
        assert self.is_element_present(*LoginPageLocators.LOGOUT_BUTTON), "Вы не авторизованы"

