import allure

from base.base_page import BasePage
from locators.locators import DashboardPageLocators


class DashboardPage(BasePage):
    locators = DashboardPageLocators()  # создаем экземпляр класса с локаторами для страницы Dashboard Page

    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self):
        self.element_is_clickable(self.locators.MY_INFO_BUTTON).click()

    @allure.step("Check items list in the left main menu")
    def check_items_list(self):
        items_list = self.get_text_from_elements(self.locators.LEFT_MENU_LIST_ITEMS)
        exp_items_list = [
            "Admin", "PIM", "Leave", "Time",
            "Recruitment", "My Info", "Performance", "Dashboard",
            "Directory", "Maintenance", "Claim", "Buzz"
        ]
        print(items_list, exp_items_list)
        assert items_list == exp_items_list, "The item names from left main are incorrect"

