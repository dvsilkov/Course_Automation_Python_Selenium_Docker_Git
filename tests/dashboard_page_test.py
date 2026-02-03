"""
Команда для запуска всех тестов с основным набором параметров:
pytest -v --alluredir=allure_results .\tests

Команда для запуска тестов из класса с основным набором параметров:
pytest -sv --alluredir=allure_results .\tests\dashboard_page_test.py::TestDashboardPage


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
    """
    Класс с тестами для проверки страницы DashboardPage
    """
    @allure.title("Checking how the DashboardPage is displayed")
    def test_dashboard_page(self):
        """
        Тест проверяет отображение элементов на странице DashboardPage
        """
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.dashboard_page.page_is_opened()
        self.sidebar_component.check_visible()
        self.topbar_component.check_visible("Dashboard")
        self.topbar_component.check_user_dropdown_items_list()
        self.dashboard_page.check_visible_time_widget()
        self.dashboard_page.check_visible_actions_widget()
        self.dashboard_page.check_visible_quick_launch_widget()
        self.dashboard_page.check_visible_posts_widget()

