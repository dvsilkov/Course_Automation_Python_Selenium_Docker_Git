from components.base_component import BaseComponent


class SidebarComponent(BaseComponent):

    # локаторы для боковой панели
    MY_INFO_ITEM = ("xpath", "//a[@href='/web/index.php/pim/viewMyDetails']")
    SIDEBAR_LIST_ITEMS = ("xpath", "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")
