import allure

from base.base_page import BasePage
from locators.locators import LoginPageLocators


class LoginPage(BasePage):
    locators = LoginPageLocators()  # создаем экземпляр класса с локаторами для страницы Login Page

    @allure.step("Enter login")
    def enter_login(self, login):
        self.element_is_clickable(self.locators.USERNAME_FIELD).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.element_is_clickable(self.locators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Click 'Submit' button")
    def click_login_button(self):
        self.element_is_clickable(self.locators.LOGIN_BUTTON).click()

    @allure.step("Get error message if Username or Password are incorrect")
    def check_error_message_wrong_credentials(self):
        error_text = self.get_text_from_element(self.locators.ERROR_MESSAGE)
        assert error_text == "Invalid credentials", f"The error text message '{error_text}' is not expected"


