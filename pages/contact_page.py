from playwright.sync_api import Page
from pages.base_page import BasePage


class ContactPage(BasePage):
    NAME_FIELD = "input[name='name'], input[placeholder*='name' i], #name"
    EMAIL_FIELD = "input[type='email'], input[name='email'], #email"
    MESSAGE_FIELD = "textarea, textarea[name='message'], #message"
    SUBMIT_BUTTON = "button[type='submit'], input[type='submit']"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.url = base_url + "/contact.html"

    def load(self) -> "ContactPage":
        self.page.goto(self.url)
        self.page.wait_for_load_state("domcontentloaded")
        return self

    def fill_name(self, text: str):
        f = self.first(self.NAME_FIELD)
        f.clear()
        f.fill(text)

    def fill_email(self, text: str):
        f = self.first(self.EMAIL_FIELD)
        f.clear()
        f.fill(text)

    def fill_message(self, text: str):
        f = self.first(self.MESSAGE_FIELD)
        f.clear()
        f.fill(text)

    def submit(self):
        self.first(self.SUBMIT_BUTTON).click()

    def fill_and_submit(self, name: str, email: str, message: str):
        self.fill_name(name)
        self.fill_email(email)
        self.fill_message(message)
        self.submit()

    def name_field_is_present(self) -> bool:
        return self.first(self.NAME_FIELD).is_visible()

    def email_field_is_present(self) -> bool:
        return self.first(self.EMAIL_FIELD).is_visible()

    def message_field_is_present(self) -> bool:
        return self.first(self.MESSAGE_FIELD).is_visible()

    def submit_button_is_enabled(self) -> bool:
        return self.first(self.SUBMIT_BUTTON).is_enabled()

    def get_email_validation_message(self) -> str:
        return self.first(self.EMAIL_FIELD).evaluate("el => el.validationMessage")

    def get_field_value(self, selector: str) -> str:
        return self.first(selector).input_value()
