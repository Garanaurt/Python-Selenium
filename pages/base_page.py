from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import math

class BasePage():
    def __init__(self, browser, url, timeout=10): #запуск и ожидание
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

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
    
    
