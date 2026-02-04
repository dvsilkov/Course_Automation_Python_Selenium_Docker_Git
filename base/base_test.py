import pytest

from components.navigation.sidebar_component import SidebarComponent
from components.navigation.topbar_component import TopbarComponent
from config.data import Data
from config.links import Links
from pages.login_page import LoginPage
from pages.personal_page import PersonalPage
from pages.proflle_image_page import ProfilePicturePage
from pages.dashboard_page import DashboardPage
from pages.buzz_page import BuzzPage


class BaseTest:
    """
    Класс для подготовки тестового окружения для всех тестовых классов
    """
    # аннотация типов
    data: Data
    links: Links
    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage
    profile_image_page: ProfilePicturePage
    buzz_page: BuzzPage
    sidebar_component: SidebarComponent
    topbar_component: TopbarComponent

    @pytest.fixture(autouse=True)
    def base(self, request, driver_fixture):
        """
        В методе base происходит инициализация драйвера и создаются экземпляры классов всех страниц.
        То есть это не нужно импортировать в тестовых классах, а к методам можно обращаться через self
        """
        request.cls.driver = driver_fixture
        request.cls.data = Data()
        request.cls.links = Links()
        request.cls.login_page = LoginPage(driver_fixture, self.links.LOGIN_PAGE)
        request.cls.dashboard_page = DashboardPage(driver_fixture, self.links.DASHBOARD_PAGE)
        request.cls.personal_page = PersonalPage(driver_fixture, self.links.PERSONAL_PAGE)
        request.cls.profile_image_page = ProfilePicturePage(driver_fixture, self.links.PROFILE_PICTURE_PAGE)
        request.cls.buzz_page = BuzzPage(driver_fixture, self.links.BUZZ_PAGE)
        request.cls.sidebar_component = SidebarComponent(driver_fixture)
        request.cls.topbar_component = TopbarComponent(driver_fixture)
