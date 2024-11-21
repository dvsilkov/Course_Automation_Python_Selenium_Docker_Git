import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function", autouse=True)  # фикстура для каждого теста, автоматически без явного указания
def driver_fixture(request):
    # браузер открывается и запускается через DriverManager
    # суть в том что драйвер будет ставиться/обновляться автоматически при вызове фикстуры
    # если Selenium 4.x
    #service = ChromeService(ChromeDriverManager().install())  # параметр для WebDriver при использовании DriverManager
    options = Options()
    # options.add_argument("--headless")  # опция для запуска в CI или Docker, локально не используется
    options.add_argument("--no-sandbox")  # позволяет браузеру обходить некоторые проверки безопасности операционной системы и снижает вероятность ошибок
    options.add_argument("--disable-dev-shm-usage")  # опция полезна, когда ограниченно кол-во физической памяти
    options.add_argument("--window-size=1920,1080")  # размер окна
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver  # драйвер устанавливается как атрибут класса request.cls. Это позволяет использовать драйвер в других методах
    yield driver
    driver.quit()
