import time

import allure
from selenium.webdriver import Keys
from base.base_page import BasePage
from locators.locators import PersonalPageLocators


class PersonalPage(BasePage):
    """
    Класс содержит методы для взаимодействия с элементами страницы DashboardPage
    """

    locators = PersonalPageLocators()  # создаем экземпляр класса с локаторами для страницы My info page

    @allure.step("Change existing name and return new name value")
    def change_name(self, new_name):
        """
        Метод добавляет в поле first_name текст и возвращает итоговое значение
        """
        with allure.step(f"The '{new_name}' text has been added to first_name field"):
            first_name_field = self.element_is_clickable(self.locators.FIRST_NAME_FIELD)
            first_name_field.send_keys(Keys.CONTROL + "a")
            first_name_field.send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(new_name)
            return new_name

    @allure.step("Click button to save changes")
    def save_changes(self):
        """
        Метод сохраняет изменения на странице PersonalPage через нажатие кнопки Save
        Также проверяет появление и исчезновение всплывающего сообщения
        """
        self.scroll_page()
        save_button = self.element_is_clickable(self.locators.SAVE_BUTTON)
        save_button.click()
        self.element_is_visible(self.locators.POP_UP_SUCCESS)
        self.element_is_not_visible(self.locators.POP_UP_SUCCESS)

    @allure.step("Name changes have been saved successfully")
    def is_name_changes_saved(self, new_name):
        """
        Метод проверяет, что изменения сохранены, путем сравнения текстового значения в элементе имени сотрудника
        """
        emp_name_label = self.element_is_visible(self.locators.EMPLOYEE_NAME)
        emp_name = emp_name_label.text
        assert emp_name.startswith(new_name), f"New first name is missing in the employee name label"

    @allure.step("Click to profile image")
    def click_profile_image(self):
        self.element_is_clickable(self.locators.PROFILE_IMAGE).click()
