import allure


from utils.urls import URL
from pages.base_page import BasePage
from locators import LoginPageLocators,MainPageLocators


class LoginPage(BasePage):
    @allure.step("Открыть страницу авторизации")
    def open_login_page(self):
        self.open_page(URL.LOGIN_PAGE)

    @allure.step("Авторизоваться")
    def login(self, email, password):
        self.send_keys_to_field(LoginPageLocators.EMAIL, email)
        self.send_keys_to_field(LoginPageLocators.PASSWORD, password)
        self.wait_for_element_hide(MainPageLocators.OVERLAY_ANIMATION)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)