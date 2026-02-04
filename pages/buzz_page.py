import allure
from datetime import datetime

from base.base_page import BasePage

class BuzzPage(BasePage):
    """
    Класс содержит локаторы и методы для взаимодействия с элементами страницы BuzzPage
    """
    # локаторы для страницы BuzzPage
    POST_BUTTON = ("xpath", "//div[@class='oxd-buzz-post-slot']/button[@type='submit']")
    POST_INPUT_FIELD = ("xpath", "//textarea[@class='oxd-buzz-post-input']")
    POP_UP_SUCCESS = ("xpath", "//div[@id='oxd-toaster_1']")
    LAST_POST_TEXT = ("xpath", "//div[@class='oxd-grid-1 orangehrm-buzz-newsfeed-posts']"
                          "/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]"
                          "//p[@class='oxd-text oxd-text--p orangehrm-buzz-post-body-text']")

    @allure.step("Check text in placeholder")
    def check_placeholder_post_field(self):
        """
        Метод для проверки текста плейсхолдера в поле Post
        """
        placeholder_text = self.element_is_visible(self.POST_INPUT_FIELD).get_attribute("placeholder")
        assert placeholder_text == "What's on your mind?", f"The placeholder text '{placeholder_text}' is incorrect, should be 'What's on your mind?'"

    @allure.step("Input text for new post")
    def input_text_post_field(self):
        """
        Метод для ввода текста в поле Post
        """
        new_post_text = f"New post at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        self.element_is_visible(self.POST_INPUT_FIELD).send_keys(new_post_text)
        return new_post_text

    @allure.step("Clck Post button")
    def click_post_button(self):
        """
        Метод для нажатия кнопки Post
        """
        self.element_is_visible(self.POST_BUTTON).click()

    @allure.step("Check that text is posted correctly")
    def is_text_posted_correctly(self, text_was_input):
        """
        Метод проверяет, что новый пост был опубликован на странице
        """
        self.element_is_visible(self.POP_UP_SUCCESS) # проверка появления всплывающего сообщения
        self.element_is_not_visible(self.POP_UP_SUCCESS) # проверка исчезновения всплывающего сообщения
        last_post_text = self.element_is_visible(self.LAST_POST_TEXT).text
        assert last_post_text == text_was_input, f"The text '{last_post_text}' is incorrect, should be '{text_was_input}'"



