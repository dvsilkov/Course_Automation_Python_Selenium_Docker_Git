"""
Команда для запуска всех тестов с основным набором параметров:
pytest -v --alluredir=allure_results .\tests

Команда для запуска тестов из класса с основным набором параметров:
>pytest -sv --alluredir=allure_results .\tests\login_page_test.py::TestLoginPage


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

    @allure.title("Input wrong credentials")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_error_message_if_wrong_credentials(self):
        self.login_page.open()
        self.login_page.enter_login(f"{self.data.LOGIN}{random.randint(1, 100)}")
        self.login_page.enter_password(f"{self.data.PASSWORD}{random.randint(1,100)}")
        self.login_page.click_login_button()
        error_text = self.login_page.get_error_message_wrong_credentials()
        self.personal_page.make_screenshot("Success")
        assert error_text == "Invalid credentials", f"The error text message '{error_text}' is not expected"
