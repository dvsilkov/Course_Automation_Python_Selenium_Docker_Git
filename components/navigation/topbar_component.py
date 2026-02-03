import allure
from components.base_component import BaseComponent


class TopbarComponent(BaseComponent):
    """
    Класс с локаторами и методами для верхней панели
    """
    # локаторы для верхней панели
    PAGE_TITLE = ("xpath", "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    USER_DROPDOWN = ("xpath", "//span[@class='oxd-userdropdown-tab']")
    USER_DROPDOWN_IMG = ("xpath", "//img[@class='oxd-userdropdown-img']")
    USER_DROPDOWN_NAME = ("xpath", "//p[@class='oxd-userdropdown-name']")
    USER_DROPDOWN_ICON = ("xpath", "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    USER_DROPDOWN_ITEMS = ("xpath", "//li/a[@class='oxd-userdropdown-link']") # находит четыре элементы

    @allure.step("Check top bar for page")
    def check_visible(self, page_name: str):
        """
        Метод проверяет отображение элементов на верхней панели
        """
        page_title = self.element_is_visible(self.PAGE_TITLE).text
        self.element_is_visible(self.USER_DROPDOWN)
        self.element_is_visible(self.USER_DROPDOWN_IMG)
        self.element_is_visible(self.USER_DROPDOWN_NAME)
        self.element_is_visible(self.USER_DROPDOWN_ICON)
        assert page_title == page_name, "The page title is incorrect"

    @allure.step("Check items list in the user dropdown")
    def check_user_dropdown_items_list(self):
        """
        Метод проверяет список разделов в боковом меню
        """
        self.element_is_visible(self.USER_DROPDOWN).click()
        dropdown_items_list = self.get_text_from_elements(self.USER_DROPDOWN_ITEMS)
        exp_dropdown_items_list = [
            'About',
            'Support',
            'Change Password',
            'Logout'
        ]
        assert dropdown_items_list == exp_dropdown_items_list, f"The item names {dropdown_items_list} from user dropdown in top bar are incorrect, should be {exp_dropdown_items_list}"
