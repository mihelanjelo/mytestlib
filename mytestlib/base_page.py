import time
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from mytestlib.basic_actions import BasicActions


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Базовый класс для PageObject объектов
class BasePage(metaclass=Singleton):

    def __init__(self, driver):
        self.driver = driver
        self.basic_actions = BasicActions(driver)

    PAGE_TITLE = None

    LOCATORS = {
        "example locator": (By.XPATH, "//button[@class='green button']"),
    }

    XPATH_PATTERNS = {
        "example pattern": "//div[text()='{text}']"
    }

    def is_page_opened(self,  waiting_time=0):
        for i in range(0, waiting_time + 1):
            if self.driver.title == self.PAGE_TITLE:
                return True
            elif i == waiting_time:
                return False
            else:
                time.sleep(1)

    def is_visible(self, locator_name, time_waiting_element=0, values=None) -> bool:
        if not values:
            return self.basic_actions.is_element_visible(self.LOCATORS[locator_name], time_waiting_element)
        else:
            locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
            return self.basic_actions.is_element_visible(locator, time_waiting_element)

    def is_not_visible(self, locator_name, time_waiting_element=0, values=None) -> bool:
        if not values:
            return self.basic_actions.wait_element_hiding(self.LOCATORS[locator_name], time_waiting_element)
        else:
            locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
            return self.basic_actions.wait_element_hiding(locator, time_waiting_element)

    def click_at(self, locator_name, time_waiting_element=0, values=None, offset=None):
        if not offset:
            if not values:
                self.basic_actions.click_on_element(self.LOCATORS[locator_name], time_waiting_element)
            else:
                locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
                self.basic_actions.click_on_element(locator, time_waiting_element)
        else:
            if not values:
                el = self.basic_actions.wait_element(self.LOCATORS[locator_name], time_waiting_element)
                action = webdriver.common.action_chains.ActionChains(self.driver)
                action.move_to_element_with_offset(el,offset['x'], offset['y'])
                action.click()
                action.perform()
            else:
                locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
                el = self.basic_actions.wait_element(locator, time_waiting_element)
                action = webdriver.common.action_chains.ActionChains(self.driver)
                action.move_to_element_with_offset(el, offset['x'], offset['y'])
                action.click()
                action.perform()
        return self

    def get_text_from(self, locator_name, time_waiting_element=0) -> str:
        if 'input' in self.LOCATORS[locator_name][1] or 'textarea' in self.LOCATORS[locator_name][1]:
            return self.basic_actions.wait_element(self.LOCATORS[locator_name], time_waiting_element). \
                get_attribute('value')
        else:
            return self.basic_actions.get_text_from_element(self.LOCATORS[locator_name], time_waiting_element)

    def get_text_from_every(self, locator_name, time_waiting_element=0) -> List[str]:
        return self.basic_actions.get_text_from_elements(self.LOCATORS[locator_name], time_waiting_element)

    def send_text_to(self, locator_name, text, time_waiting_element=0, values=None):
        if not values:
            self.basic_actions.send_text_to_element(text, self.LOCATORS[locator_name], time_waiting_element)
        else:
            locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
            print(locator)
            self.basic_actions.send_text_to_element(text, locator, time_waiting_element)
        return self

    def clear(self, locator_name, time_waiting_element=0):
        self.basic_actions.wait_element(self.LOCATORS[locator_name], time_waiting_element).clear()
        return self

    def select_item(self, locator_name, value, time_waiting_element=0):
        self.basic_actions.select_item_by_text(value, self.LOCATORS[locator_name], time_waiting_element)
        return self

    def get_elements(self, locator_name, time_waiting_element=0, values=None) -> List[WebElement]:
        if not values:
            return self.basic_actions.wait_elements(self.LOCATORS[locator_name], time_waiting_element)
        else:
            locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
            return self.basic_actions.wait_elements(locator, time_waiting_element)

    def get_element(self, locator_name, time_waiting_element=0, values=None) -> WebElement:
        if not values:
            return self.basic_actions.wait_element(self.LOCATORS[locator_name], time_waiting_element)
        else:
            locator = (By.XPATH, self.XPATH_PATTERNS[locator_name].format(**values))
            return self.basic_actions.wait_element(locator, time_waiting_element)
