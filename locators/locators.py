"""
Основной подход, внутри можно создать классы, соответствующие каждому классу PageObject:
Для каждого селектора создаем кортеж, теперь каждый селектор — это пара: как искать и что искать.
"""


class LoginPageLocators:
    """ Класс с локаторами для страницы 'Login page ' """
    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    LOGIN_BUTTON = ("xpath", "//button[@type='submit']")


class DashboardPageLocators:
    """ Класс с локаторами для страницы 'Dashboard page ' """
    MY_INFO_BUTTON = ("xpath", "//a[@href='/web/index.php/pim/viewMyDetails']")


class PersonalPageLocators:
    """ Класс с локаторами для страницы 'My info page ' """
    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "//button[@type='submit']")
    POP_UP_SUCCESS = ("xpath", "//div[@id='oxd-toaster_1']")
