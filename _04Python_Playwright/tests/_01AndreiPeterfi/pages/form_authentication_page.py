from tests._01AndreiPeterfi.pages.base_page import BasePage


class FormAuthenticationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_field_locator = page.locator("#username")
        self.password_field_locator = page.locator("#password")
        self.btn_login = page.locator("#login button")

    def setUsernameAndPassword(self, username: str, password: str):
        self.username_field_locator.type(username)
        self.password_field_locator.type(password)
        self.btn_login.click()
