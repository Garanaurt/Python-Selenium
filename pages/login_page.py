from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self): #проверка это страница логин или нет
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.url, 'Не та страница'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина отсутствует"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Форма регистрации отсутствует"

    def register_new_user(self, mail, password): # заполнение регисрационной формы
        self.mail_add_to_reg_form(*LoginPageLocators.REG_MAIL_FORM, mail)
        self.password_add_to_form(*LoginPageLocators.REG_PASS_FORM, password)
        self.passw2_add_to_reg_form(*LoginPageLocators.REG_PASS_FORM_2, password)
        self.registration_button(*LoginPageLocators.REG_BUTTON)
        