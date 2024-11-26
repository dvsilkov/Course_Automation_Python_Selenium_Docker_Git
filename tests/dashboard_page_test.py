"""
Команда для запуска всех тестов с основным набором параметров:
pytest -v --alluredir=allure_results .\tests

Команда для запуска тестов из класса с основным набором параметров:
>pytest -sv --alluredir=allure_results .\tests\dashboard_page_test.py::TestDashboardPage


Команда для запуска отчета Allure:
allure serve .\allure_results

Команда для генерации файла отчета Allure:
allure generate allure_results --clean -o allure_report
"""
import random

import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Dashboard Page Functionality")
class TestDashboardPage(BaseTest):

    @allure.title("The checking that main left menu has correct item names")
    @allure.severity("Medium")
    @pytest.mark.smoke
    def test_item_names_from_main_menu(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.dashboard_page.check_items_list()
        self.personal_page.make_screenshot("Success")

