from tests._01AndreiPeterfi.pages.base_page import (BasePage)


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.list_locator = page.locator("ul li")

    def getNoOfListElements(self):
        return self.list_locator.count()

    def navigate_to_page(self, page, page_to_navigate: str):
        element = self.page.get_by_text(page_to_navigate)
        element.click()
