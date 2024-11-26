"""
Команда для запуска тестов с основным набором параметров:
pytest -v --alluredir=\allure_results .\tests

Команда для запуска отчета Allure:
allure serve .\allure_results

Команда для генерации файла отчета Allure:
allure generate allure_results --clean -o allure_report
"""
import random
import time

import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.dashboard_page.page_is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.page_is_opened()
        new_name = self.personal_page.change_name(f"_Test_{random.randint(1, 100)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved(new_name)
        self.personal_page.make_screenshot("Success")
