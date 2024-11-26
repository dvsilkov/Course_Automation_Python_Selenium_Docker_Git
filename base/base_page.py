import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, page_url):
        """
        Конструктор класса объявляется ключевым словом __init__. В него в качестве параметров передаются
        экземпляр драйвера. Внутри конструктора эти данные хранятся как атрибуты класса.
        """
        self.driver = driver
        self.page_url = page_url
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)  # таймаут - 10 сек, частота поиска - 1 сек

    @allure.step(f"Open page")
    def open(self):
        """ Метод open. Он открывает нужную страницу в браузере, используя метод get() """
        self.driver.get(self.page_url)

    @allure.step(f"Page is opened")
    def page_is_opened(self):
        """ Метод is_opened вернет True, если текущий URL страницы станет равным self.PAGE_URL. """
        self.wait.until(EC.url_to_be(self.page_url), message=f"Current URL is not equal '{self.page_url}'")  # ожидает, пока URL страницы не станет равным указанному URL

    @allure.step(f"Screenshot has been created")
    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    def element_is_clickable(self, locator):
        """
        Метод находит и возвращает веб-элемент, когда он станет готов к нажатию на него. Поиск элемента идет по локатору.
        В методе реализован механизм явного ожидания. То есть поиск элемента продолжается в пределах заданного таймаута,
        по истечении которого вызывается исключение 'TimeoutException'.
        """
        # возвращает элемент
        with allure.step(f"Web-element '{locator}' has been found"):
            return self.wait.until(EC.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}")

    def text_is_present_in_element(self, locator, exp_text):
        """
        Метод находит и возвращает веб-элемент, если нужный текст появится в значении элемента.
        Поиск элемента идет по локатору.
        В методе реализован механизм явного ожидания. То есть поиск элемента продолжается в пределах заданного таймаута,
        по истечении которого вызывается исключение 'TimeoutException'.
        """
        # возвращает элемент
        with allure.step(f"Web-element '{locator}' has been found and value '{exp_text}'appeared"):
            return self.wait.until(EC.text_to_be_present_in_element_value(locator, exp_text), message=f"Can't find element by locator {locator}")

    def element_is_visible(self, locator):
        """
        Метод находит и возвращает веб-элемент, когда он станет виден на странице. Поиск элемента идет по локатору.
        В методе реализован механизм явного ожидания. То есть поиск элемента продолжается в пределах заданного таймаута,
        по истечении которого вызывается исключение 'TimeoutException'.
        """
        # возвращает элемент
        return self.wait.until(EC.visibility_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def element_is_not_visible(self, locator):
        """
        Метод находит и возвращает веб-элемент, когда он исчезнет на странице. Поиск элемента идет по локатору.
        В методе реализован механизм явного ожидания. То есть поиск элемента продолжается в пределах заданного таймаута,
        по истечении которого вызывается исключение 'TimeoutException'.
        """
        # возвращает элемент
        return self.wait.until(EC.invisibility_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def get_text_from_element(self, locator):
        """
        Метод находит элемент по локатору и возвращает текстовое значение из него.
        """
        return self.element_is_visible(locator)
