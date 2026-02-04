"""
Команда для запуска всех тестов с основным набором параметров:
pytest -v --alluredir=allure_results .\tests

Команда для запуска тестов из класса с основным набором параметров:
pytest -sv --alluredir=allure_results .\tests\buzz_page_test.py::TestBuzzPage


Команда для запуска отчета Allure:
allure serve .\allure_results

Команда для генерации файла отчета Allure:
allure generate allure_results --clean -o allure_report
"""
import random

import allure
from base.base_test import BaseTest


@allure.feature("Buzz Page Functionality")
class TestBuzzPage(BaseTest):
    """
    Класс с тестами для проверки страницы BuzzPage
    """
    @allure.title("The adding a new post and checking it on the page")
    def test_add_new_post(self):
        """
        Тест выполняет размещение нового поста и проверяет его отображение в списке на странице BuzzPage
        """
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.dashboard_page.page_is_opened()
        self.sidebar_component.click_buzz_link()
        self.buzz_page.page_is_opened()
        self.sidebar_component.check_visible()
        self.topbar_component.check_visible("Buzz")
        self.topbar_component.check_user_dropdown_items_list()
        self.buzz_page.check_placeholder_post_field()
        input_text = self.buzz_page.input_text_post_field()
        self.buzz_page.click_post_button()
        self.buzz_page.is_text_posted_correctly(input_text)
        self.buzz_page.make_screenshot("Success")

