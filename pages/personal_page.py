import allure
from base.base_page import BasePage
from locators.locators import PersonalPageLocators


class PersonalPage(BasePage):
    locators = PersonalPageLocators()  # создаем экземпляр класса с локаторами для страницы My info page

    @allure.step("Change existing name and return new name value")
    def change_name(self, add_to_name):
        with allure.step(f"The '{add_to_name}' text has been added to first name"):
            first_name_field = self.element_is_clickable(self.locators.FIRST_NAME_FIELD)
            first_name_field.send_keys(add_to_name)
            new_name = first_name_field.text
            return new_name

    @allure.step("Click button to save changes")
    def save_changes(self):
        self.element_is_clickable(self.locators.SAVE_BUTTON).click()

    @allure.step("Changes have been saved successfully")
    def is_changes_saved(self, new_name):
        self.element_is_visible(self.locators.POP_UP_SUCCESS)
        self.element_is_not_visible(self.locators.POP_UP_SUCCESS)
        self.text_is_present_in_element(self.locators.FIRST_NAME_FIELD, new_name)

    @allure.step("Click to profile image")
    def click_profile_image(self):
        self.element_is_clickable(self.locators.PROFILE_IMAGE).click()
