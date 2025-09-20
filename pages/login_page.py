import allure

from locators import LoginPageLocators
from pages.base_page import BasePage
from data.urls import login_site



class LoginPage(BasePage):


    @allure.step('Открыть страницу авторизации')
    def open_login_page(self):
        self.open_page(login_site)

    @allure.step("Авторизоваться")
    def login(self, email, password):
        self.wait_for_element_clickable(LoginPageLocators.EMAIL_FIELD)
        self.send_keys_to_input(LoginPageLocators.EMAIL_FIELD, email)
        self.send_keys_to_input(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_on_element(LoginPageLocators.BUT_ENTER)