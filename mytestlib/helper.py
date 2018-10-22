from mytestlib.base_page import BasePage


driver = None


def on(page: str) -> BasePage:
    return globals()[page](driver)

