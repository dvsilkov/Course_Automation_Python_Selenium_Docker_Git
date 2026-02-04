import allure
from components.base_component import BaseComponent


class SidebarComponent(BaseComponent):
    """
    Класс с локаторами и методами для боковой панели
    """
    # локаторы для боковой панели
    SIDEBAR_BANNER = ("xpath", "//div[@class='oxd-brand-banner']")
    SIDEBAR_BANNER_URL = ("xpath", "//a[@href='https://www.orangehrm.com/']")

    MY_INFO_ITEM = ("xpath", "//a[@href='/web/index.php/pim/viewMyDetails']")
    BUZZ_ITEM = ("xpath", "//a[@href='/web/index.php/buzz/viewBuzz']")

    SIDEBAR_ITEMS = ("xpath", "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")

    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self):
        self.element_is_clickable(self.MY_INFO_ITEM).click()

    @allure.step("Click on 'Buzz' link")
    def click_buzz_link(self):
        self.element_is_clickable(self.BUZZ_ITEM).click()

    @allure.step("Check items list in the left main menu")
    def check_visible(self):
        """
        Метод проверяет отображение элементов и список разделов в боковом меню
        """
        self.element_is_visible(self.SIDEBAR_BANNER)
        sidebar_url = self.element_is_visible(self.SIDEBAR_BANNER_URL).get_attribute("href")
        items_list = self.get_text_from_elements(self.SIDEBAR_ITEMS)
        exp_items_list = [
            "Admin", "PIM", "Leave", "Time",
            "Recruitment", "My Info", "Performance", "Dashboard",
            "Directory", "Maintenance", "Claim", "Buzz"
        ]
        assert sidebar_url == "https://www.orangehrm.com/", f"The sidebar url '{sidebar_url}' is incorrect, should be 'https://www.orangehrm.com/'"
        assert items_list == exp_items_list, "The item names from left menu are incorrect"
