"""
Contact form tests for luxival.vercel.app/contact.html
Covers: field presence, input, browser validation, keyboard interaction.
Playwright-specific: input_value(), evaluate() for validationMessage, Tab key.
"""
import pytest
from pages.contact_page import ContactPage

VALID_NAME = "Test User"
VALID_EMAIL = "testuser@example.com"
VALID_MESSAGE = "This is an automated test message sent by the Playwright QA suite."


class TestContactFormPresence:
    def test_name_field_is_present(self, contact_page):
        assert contact_page.name_field_is_present(), "Name input field not found"

    def test_email_field_is_present(self, contact_page):
        assert contact_page.email_field_is_present(), "Email input field not found"

    def test_message_field_is_present(self, contact_page):
        assert contact_page.message_field_is_present(), "Message textarea not found"

    def test_submit_button_is_enabled(self, contact_page):
        assert contact_page.submit_button_is_enabled(), (
            "Submit button should be enabled on load"
        )


class TestContactFormValidation:
    def test_invalid_email_triggers_browser_validation(self, contact_page):
        contact_page.fill_name(VALID_NAME)
        contact_page.fill_email("not-an-email")
        contact_page.fill_message(VALID_MESSAGE)
        contact_page.submit()
        msg = contact_page.get_email_validation_message()
        assert msg != "", (
            "Browser should report a validation error for an invalid email address"
        )

    def test_empty_email_triggers_browser_validation(self, contact_page):
        contact_page.fill_name(VALID_NAME)
        contact_page.fill_email("")
        contact_page.fill_message(VALID_MESSAGE)
        contact_page.submit()
        msg = contact_page.get_email_validation_message()
        assert msg != "", (
            "Browser should report a validation error when email is empty"
        )

    def test_email_with_missing_domain_is_invalid(self, contact_page):
        contact_page.fill_name(VALID_NAME)
        contact_page.fill_email("user@")
        contact_page.fill_message(VALID_MESSAGE)
        contact_page.submit()
        msg = contact_page.get_email_validation_message()
        assert msg != "", "Email 'user@' (missing domain) should fail browser validation"


class TestContactFormInput:
    def test_name_field_accepts_text(self, contact_page):
        contact_page.fill_name(VALID_NAME)
        value = contact_page.get_field_value(contact_page.NAME_FIELD)
        assert value == VALID_NAME

    def test_email_field_accepts_valid_email(self, contact_page):
        contact_page.fill_email(VALID_EMAIL)
        value = contact_page.get_field_value(contact_page.EMAIL_FIELD)
        assert value == VALID_EMAIL

    def test_message_field_accepts_text(self, contact_page):
        contact_page.fill_message(VALID_MESSAGE)
        value = contact_page.get_field_value(contact_page.MESSAGE_FIELD)
        assert value == VALID_MESSAGE

    def test_fields_can_be_cleared_and_refilled(self, contact_page):
        contact_page.fill_name("First Entry")
        contact_page.fill_name(VALID_NAME)
        value = contact_page.get_field_value(contact_page.NAME_FIELD)
        assert value == VALID_NAME

    def test_tab_key_moves_focus_between_fields(self, contact_page, page):
        page.locator(contact_page.NAME_FIELD).first.click()
        page.keyboard.press("Tab")
        focused_type = page.evaluate(
            "() => document.activeElement ? document.activeElement.type : ''"
        )
        assert focused_type == "email", (
            f"Tab from name field should focus email field, got type: '{focused_type}'"
        )


class TestContactPageLoad:
    def test_contact_page_url_is_correct(self, contact_page):
        assert "contact" in contact_page.current_url.lower(), (
            f"Expected 'contact' in URL, got: {contact_page.current_url}"
        )

    def test_contact_page_title_is_not_empty(self, contact_page):
        assert contact_page.title.strip() != "", "Contact page title should not be empty"
