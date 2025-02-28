from tests._01AndreiPeterfi.pages.form_authentication_page import FormAuthenticationPage
from tests._01AndreiPeterfi.pages.home_page import HomePage


class TestFormAuthentication:
    def test_form_authentication_page_title(self, page):
        homePage = HomePage(page)
        homePage.goto("https://the-internet.herokuapp.com/")
        homePage.navigate_to_page("Form Authentication")
        assert page.title() == "The Internet"

    def test_succesfull_login(self, page):
        homePage = HomePage(page)
        homePage.goto("https://the-internet.herokuapp.com/")
        homePage.navigate_to_page("Form Authentication")
        formAuthenticationPage = FormAuthenticationPage(page)
        formAuthenticationPage.setUsernameAndPassword("tomsmith", "SuperSecretPassword!")

    def test_navigate_to_another_page(self, page):
        homePage = HomePage(page)
        homePage.goto("https://the-internet.herokuapp.com/")
        homePage.navigate_to_page("A/B Testing")
        assert page.title() == "The Internet"
