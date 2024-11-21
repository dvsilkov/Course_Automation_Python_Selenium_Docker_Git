import allure

from base.base_page import BasePage
from locators.locators import DashboardPageLocators


class DashboardPage(BasePage):
    locators = DashboardPageLocators()  # создаем экземпляр класса с локаторами для страницы Dashboard Page

    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self):
        self.element_is_clickable(self.locators.MY_INFO_BUTTON).click()

