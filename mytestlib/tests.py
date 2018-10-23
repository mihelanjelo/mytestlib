import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from mytestlib.base_page import BasePage
from mytestlib.helper import Helper


class MockPage(BasePage):
    PAGE_TITLE = 'TIOBE Index | TIOBE - The Software Quality Company'
    LOCATORS = {
        "Java": (By.XPATH, "//td[contains(text(), 'Java')]"),
        "Detailed view on java": (By.XPATH, "//b[contains(text(), 'The Java Programming Language')]"),
    }


class TestBasePage(unittest.TestCase):

    def test_base_page(self):
        helper = Helper(webdriver.Chrome())
        on = helper.on_page
        helper.visit('https://www.tiobe.com/tiobe-index/')
        assert on(MockPage).is_page_opened(5)
        assert on(MockPage).click_at('Java', 3).is_visible('Detailed view on java', 3)
        helper.quit()
