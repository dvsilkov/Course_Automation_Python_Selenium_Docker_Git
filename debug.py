from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

service = Service(executable_path=ChromeDriverManager().install())
options = Options()
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com/")
driver.quit()