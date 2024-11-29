"""
Команда для запуска всех тестов с основным набором параметров:
pytest -v --alluredir=allure_results .\tests

Команда для запуска тестов из класса с основным набором параметров:
pytest -sv --alluredir=allure_results .\tests\profile_picture_test.py::TestProfilePicture


Команда для запуска отчета Allure:
allure serve .\allure_results

Команда для генерации файла отчета Allure:
allure generate allure_results --clean -o allure_report
"""
import random

import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Profile Picture Page Functionality")
class TestProfilePicture(BaseTest):

    @allure.title("Update profile picture")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_update_profile_picture(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.dashboard_page.page_is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.page_is_opened()
        self.personal_page.click_profile_image()
        self.profile_image_page.page_is_opened()
        self.profile_image_page.upload_new_image()
        self.profile_image_page.is_image_uploaded()
        self.profile_image_page.save_changes()
        self.profile_image_page.is_changes_saved()
        self.profile_image_page.make_screenshot("Success")
