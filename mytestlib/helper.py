from mytestlib.base_page import BasePage


driver = None


def on(page_name):
    for page in BasePage.__subclasses__():
        if page.__name__ == page_name:
            return page(driver)

