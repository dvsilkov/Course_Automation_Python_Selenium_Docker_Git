"""
Команда для запуска всех тестов с основным набором параметров:
pytest -v --alluredir=allure_results .\tests

Команда для запуска тестов из класса с основным набором параметров:
pytest -sv --alluredir=allure_results .\tests\login_page_test.py::TestLoginPage


Команда для запуска отчета Allure:
allure serve .\allure_results

Команда для генерации файла отчета Allure:
allure generate allure_results --clean -o allure_report
"""
import random

import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Login Page Functionality")
class TestLoginPage(BaseTest):
    """
    Класс с тестами для проверки страницы LoginPage
    """
    @allure.title("Input wrong credentials")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_error_message_if_wrong_credentials(self):
        """
        Тест проверяет сообщение при вводе неверных учетных данных
        """
        self.login_page.open()
        self.login_page.enter_login(f"{self.data.LOGIN}{random.randint(1, 100)}")
        self.login_page.enter_password(f"{self.data.PASSWORD}{random.randint(1,100)}")
        self.login_page.click_login_button()
        self.login_page.check_error_message_wrong_credentials()
        self.personal_page.make_screenshot("Success")

    @allure.title("Successful login and Dashboard Page by default")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_open_dashboard_after_login(self):
        """
        Тест проверяет, что при успешном логине открывается страница Dashboard
        """
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.dashboard_page.page_is_opened()
        self.dashboard_page.make_screenshot("Success")

    @allure.title("The checking that main left menu has correct item names")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_item_names_from_main_menu(self):
        """
        Тест проверяет список разделов в боковом меню
        """
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.dashboard_page.page_is_opened()
        self.sidebar_component.check_visible()
        self.dashboard_page.make_screenshot("Success")



