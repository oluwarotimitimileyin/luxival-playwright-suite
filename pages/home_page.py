from playwright.sync_api import Page
from pages.base_page import BasePage


class HomePage(BasePage):
    NAV_LINKS = "nav a"
    HERO_HEADING = "h1"
    SERVICE_CARDS = ".service-card, .card, [class*='service'], [class*='card']"
    FOOTER = "footer"
    FOOTER_LINKS = "footer a"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.url = base_url + "/"

    def load(self) -> "HomePage":
        self.page.goto(self.url)
        self.page.wait_for_load_state("domcontentloaded")
        return self

    def get_nav_links(self):
        return self.all(self.NAV_LINKS)

    def hero_heading_text(self) -> str:
        return self.first(self.HERO_HEADING).inner_text()

    def get_service_cards(self):
        return self.all(self.SERVICE_CARDS)

    def is_footer_visible(self) -> bool:
        footer = self.first(self.FOOTER)
        footer.scroll_into_view_if_needed()
        return footer.is_visible()

    def get_footer_links(self):
        return self.all(self.FOOTER_LINKS)
