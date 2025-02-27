from tests._01AndreiPeterfi.pages.home_page import HomePage


class TestHome:
    def test_home_page_title(self, page):
        homePage = HomePage(page)
        homePage.goto("https://the-internet.herokuapp.com/")
        assert (
            page.title() == "The Internet"
        )

    def test_no_of_list_elements(self, page):
        homePage = HomePage(page)
        homePage.goto("https://the-internet.herokuapp.com/")
        assert homePage.getNoOfListElements() == 44

    def test_navigate_to_another_page(self, page):
        homePage = HomePage(page)
        homePage.goto("https://the-internet.herokuapp.com/")
        homePage.navigate_to_page(page, "A/B Testing")
        assert (
            page.title() == "The Internet"
        )
