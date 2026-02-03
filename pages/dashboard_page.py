import allure

from base.base_page import BasePage

class DashboardPage(BasePage):
    """
    Класс содержит локаторы и методы для взаимодействия с элементами страницы DashboardPage
    """
    # локаторы для страницы DashboardPage
    TIME_WIDGET = ("xpath", "//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-dashboard-widget'][1]")
    TIME_WIDGET_NAME = ("xpath", "//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-dashboard-widget'][1]/div/div/div/p")

    ACTIONS_WIDGET = ("xpath", "//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-dashboard-widget'][2]")
    ACTIONS_WIDGET_NAME = ("xpath","//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-dashboard-widget'][2]/div/div/div/p")

    QUICK_LAUNCH_WIDGET = ("xpath", "//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-dashboard-widget'][3]")
    QUICK_LAUNCH_WIDGET_NAME = ("xpath","//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-dashboard-widget'][3]/div/div/div/p")

    POSTS_WIDGET = ("xpath", "//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-dashboard-widget'][4]")
    POSTS_WIDGET_NAME = ("xpath","//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-dashboard-widget'][4]/div/div/div/p")

    @allure.step("Checking the display time widget")
    def check_visible_time_widget(self):
        """
        Метод для проверки отображения виджета Time at Work
        """
        self.element_is_visible(self.TIME_WIDGET)
        widget_name = self.element_is_visible(self.TIME_WIDGET_NAME).text
        assert widget_name == "Time at Work", f"The widget name '{widget_name}' is incorrect, should be 'Time at Work'"

    @allure.step("Checking the display actions widget")
    def check_visible_actions_widget(self):
        """
        Метод для проверки отображения виджета My Actions
        """
        self.element_is_visible(self.ACTIONS_WIDGET)
        widget_name = self.element_is_visible(self.ACTIONS_WIDGET_NAME).text
        assert widget_name == "My Actions", f"The widget name '{widget_name}' is incorrect, should be 'My Actions'"

    @allure.step("Checking the display quick launch widget")
    def check_visible_quick_launch_widget(self):
        """
        Метод для проверки отображения виджета Quick Launch
        """
        self.element_is_visible(self.QUICK_LAUNCH_WIDGET)
        widget_name = self.element_is_visible(self.QUICK_LAUNCH_WIDGET_NAME).text
        assert widget_name == "Quick Launch", f"The widget name '{widget_name}' is incorrect, should be 'Quick Launch'"

    @allure.step("Checking the display latest posts widget")
    def check_visible_posts_widget(self):
        """
        Метод для проверки отображения виджета Buzz Latest Posts
        """
        self.element_is_visible(self.POSTS_WIDGET)
        widget_name = self.element_is_visible(self.POSTS_WIDGET_NAME).text
        assert widget_name == "Buzz Latest Posts", f"The widget name '{widget_name}' is incorrect, should be 'Buzz Latest Posts'"