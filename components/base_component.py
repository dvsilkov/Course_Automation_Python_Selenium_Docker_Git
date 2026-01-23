from selenium.webdriver.support.wait import WebDriverWait


class BaseComponent:
    """
    В классе инициализируется драйвер и размещены общие методы для всех страниц
    """

    def __init__(self, driver, page_url):
        """
        Конструктор класса объявляется ключевым словом __init__. В него в качестве параметров передаются
        экземпляр драйвера. Внутри конструктора эти данные хранятся как атрибуты класса.
        """
        self.driver = driver
        self.page_url = page_url
        self.wait = WebDriverWait(driver, timeout=20, poll_frequency=1)  # тайм-аут - 10 сек, частота опроса страницы - 1 сек