from mytestlib.base_page import BasePage


class Helper:
    def __init__(self, driver):
        self.driver = driver

    def on_page(self, page) -> BasePage:
        return page(self.driver)

    def visit(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()

