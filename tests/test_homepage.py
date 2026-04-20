"""
Homepage tests for luxival.vercel.app
Covers: page load, title, navigation, hero section, service cards, footer.
Playwright-specific: network idle wait, scroll-into-view, cross-browser.
"""
import pytest
from pages.home_page import HomePage


class TestHomepageLoad:
    def test_page_title_is_not_empty(self, home_page):
        assert home_page.title.strip() != "", "Page title should not be empty"

    def test_page_title_contains_luxival(self, home_page):
        assert "luxival" in home_page.title.lower(), (
            f"Expected 'luxival' in title, got: '{home_page.title}'"
        )

    def test_url_resolves_to_base(self, home_page):
        assert "luxival.vercel.app" in home_page.current_url

    def test_page_has_no_console_errors(self, home_page, page):
        errors = []
        page.on("pageerror", lambda err: errors.append(str(err)))
        page.reload()
        page.wait_for_load_state("domcontentloaded")
        assert errors == [], f"Console errors on load: {errors}"


class TestNavigation:
    def test_navigation_links_exist(self, home_page):
        links = home_page.get_nav_links()
        assert len(links) > 0, "No navigation links found"

    def test_all_nav_links_have_href(self, home_page):
        links = home_page.get_nav_links()
        for link in links:
            href = link.get_attribute("href")
            assert href, f"Nav link '{link.inner_text()}' is missing an href"

    def test_no_nav_links_point_to_hash_only(self, home_page):
        links = home_page.get_nav_links()
        bad = [l.get_attribute("href") for l in links if l.get_attribute("href") == "#"]
        assert bad == [], f"Found {len(bad)} nav link(s) with bare '#' href"


class TestHeroSection:
    def test_hero_heading_is_visible(self, home_page):
        text = home_page.hero_heading_text()
        assert text.strip() != "", "Hero heading (h1) should not be empty"

    def test_hero_heading_is_meaningful(self, home_page):
        text = home_page.hero_heading_text()
        assert len(text) > 5, f"Hero heading too short: '{text}'"


class TestServiceCards:
    def test_service_cards_present(self, home_page):
        cards = home_page.get_service_cards()
        assert len(cards) > 0, "No service cards found on homepage"

    def test_multiple_services_shown(self, home_page):
        cards = home_page.get_service_cards()
        assert len(cards) >= 2, (
            f"Expected at least 2 service cards, found {len(cards)}"
        )


class TestFooter:
    def test_footer_is_visible(self, home_page):
        assert home_page.is_footer_visible(), "Footer should be visible after scroll"

    def test_footer_contains_links(self, home_page):
        links = home_page.get_footer_links()
        assert len(links) > 0, "Footer should contain at least one link"

    def test_footer_links_have_href(self, home_page):
        links = home_page.get_footer_links()
        for link in links:
            href = link.get_attribute("href")
            assert href and href != "#", (
                f"Footer link '{link.inner_text()}' has missing or bare href"
            )


class TestPagePerformance:
    def test_page_loads_within_threshold(self, page, base_url):
        with page.expect_event("load"):
            start = page.evaluate("() => Date.now()")
            page.goto(base_url + "/")
        end = page.evaluate("() => Date.now()")
        duration_ms = end - start
        assert duration_ms < 10000, f"Page took {duration_ms}ms to load (threshold: 10s)"
