from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    @property
    def title(self) -> str:
        return self.page.title()

    @property
    def current_url(self) -> str:
        return self.page.url

    def locator(self, selector: str):
        return self.page.locator(selector)

    def first(self, selector: str):
        return self.page.locator(selector).first

    def all(self, selector: str):
        return self.page.locator(selector).all()
