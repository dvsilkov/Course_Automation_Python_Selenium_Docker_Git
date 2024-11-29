import allure
from base.base_page import BasePage
from locators.locators import ProfilePicturePageLocators


class ProfilePicturePage(BasePage):
    locators = ProfilePicturePageLocators()  # создаем экземпляр класса с локаторами для страницы Profile Picture page

    @allure.step("Upload new image to profile")
    def upload_new_image(self):
        current_directory = os.getcwd()  # получаем текущий рабочий каталог
        path_to_image = rf"{current_directory}\Profile_Image.png"
        print(path_to_image)
        upload_image = self.element_is_present(self.locators.UPLOAD_BUTTON)
        upload_image.send_keys(path_to_image)

    @allure.step("Picture has been uploaded successfully")
    def is_image_uploaded(self):
        # суть проверки в том, что после загрузки изображения найден элемент с атрибутом src и нужным значением
        self.element_is_visible(self.locators.NEW_IMAGE)

    @allure.step("Click button to save changes")
    def save_changes(self):
        self.element_is_clickable(self.locators.SAVE_BUTTON).click()

    @allure.step("Picture has been updated successfully")
    def is_changes_saved(self):
        self.element_is_visible(self.locators.POP_UP_SUCCESS)
        self.element_is_not_visible(self.locators.POP_UP_SUCCESS)
