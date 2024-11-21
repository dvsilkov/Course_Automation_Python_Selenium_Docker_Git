import pytest
from config.data import Data
from config.links import Links
from pages.login_page import LoginPage
from pages.personal_page import PersonalPage
from pages.dashboard_page import DashboardPage


class BaseTest:
    # аннотация типов
    data: Data
    links: Links
    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage

    @pytest.fixture(autouse=True)
    def base(self, request, driver_fixture):
        request.cls.driver = driver_fixture
        request.cls.data = Data()
        request.cls.links = Links()
        request.cls.login_page = LoginPage(driver_fixture, self.links.LOGIN_PAGE)
        request.cls.dashboard_page = DashboardPage(driver_fixture, self.links.DASHBOARD_PAGE)
        request.cls.personal_page = PersonalPage(driver_fixture, self.links.PERSONAL_PAGE)

