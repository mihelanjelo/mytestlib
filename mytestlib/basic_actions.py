import time
import inspect
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
last_wanted_element_info = None


# Класс c базовыми действиями над элементами страниц
class BasicActions:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            WebDriverWait(self.driver, time_waiting_element). \
                until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            raise TimeoutException('Элемент не обнаружен!')

    def send_text_to_element(self, text, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            element = WebDriverWait(self.driver, time_waiting_element). \
                until(EC.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            raise TimeoutException('Элемент не обнаружен!')

    def select_item_by_text(self, text, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            select = Select(self.wait_element(locator, time_waiting_element))
            select.select_by_visible_text(text)
        except TimeoutException:
            raise TimeoutException('Элемент не обнаружен!')

    def get_text_from_element(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            element = WebDriverWait(self.driver, time_waiting_element). \
                until(EC.presence_of_element_located(locator))
            return element.text
        except TimeoutException:
            raise TimeoutException('Элемент не обнаружен!')

    def get_text_from_elements(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            elements = WebDriverWait(self.driver, time_waiting_element). \
                until(EC.presence_of_all_elements_located(locator))
            texts = []
            for element in elements:
                try:
                    texts.append(element.text.strip())
                except StaleElementReferenceException:
                    continue
            return texts
        except TimeoutException:

            raise TimeoutException('Элемент не обнаружен!')

    def get_element_color(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            element = WebDriverWait(self.driver, time_waiting_element). \
                until(EC.presence_of_element_located(locator))
            return element.value_of_css_property('background-color')
        except TimeoutException:
            raise TimeoutException('Элемент не обнаружен!')

    def is_element_visible(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            WebDriverWait(self.driver, time_waiting_element). \
                until(EC.visibility_of_element_located(
                locator))
            return True
        except TimeoutException:
            return False

    def is_element_in_dom(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            WebDriverWait(self.driver, time_waiting_element). \
                until(EC.presence_of_element_located(
                locator))
            return True
        except TimeoutException:
            return False

    def is_element_clickable(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            WebDriverWait(self.driver, time_waiting_element). \
                until(EC.element_to_be_clickable(
                locator))
            return True
        except TimeoutException:
            return False

    def wait_element_hiding(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            for i in range(0, time_waiting_element + 1):
                if i == time_waiting_element:
                    return False
                WebDriverWait(self.driver, 1). \
                    until(EC.visibility_of_element_located(
                    locator))
                time.sleep(1)

        except TimeoutException:
            return True

    def are_elements_visible(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            WebDriverWait(self.driver, time_waiting_element). \
                until(EC.visibility_of_any_elements_located(
                locator))
            return True
        except TimeoutException:
            return False

    def wait_element(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            return WebDriverWait(self.driver, time_waiting_element).until(EC.visibility_of_element_located(
                locator))
        except TimeoutException:
            raise TimeoutException('Элемент не обнаружен!')

    def wait_invisible_element(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            return WebDriverWait(self.driver, time_waiting_element).until(EC.presence_of_element_located(
                locator))
        except TimeoutException:
            raise TimeoutException('Элемент не обнаружен!')

    def wait_elements(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            for i in range(0, time_waiting_element + 1):
                try:
                    elements = WebDriverWait(self.driver, time_waiting_element).until(
                        EC.visibility_of_any_elements_located(
                            locator))
                    return elements
                except StaleElementReferenceException:
                    time.sleep(1)
                if i == time_waiting_element:
                    return []
        except TimeoutException:
            return []

    def wait_invisible_elements(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            for i in range(0, time_waiting_element + 1):
                try:
                    elements = WebDriverWait(self.driver, time_waiting_element).until(
                        EC.presence_of_all_elements_located(
                            locator))
                    return elements
                except StaleElementReferenceException:
                    time.sleep(1)
                if i == time_waiting_element:
                    return []
        except TimeoutException:
            return []

    def wait_element_clickable(self, locator, time_waiting_element=0):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.set_log_element_info(calframe, locator)
        try:
            return WebDriverWait(self.driver, time_waiting_element).until(EC.element_to_be_clickable(
                locator))
        except TimeoutException:
            raise TimeoutException('Элемент не обнаружен!')

    def set_log_element_info(self, calframe, locator):
        global last_wanted_element_info
        last_wanted_element_info = """Сведения о последнем искомом элементе: {{
             caller's file_name: {file_name}
             caller's locator: {locator}
             caller's func_name: {func_name}
             caller's context: {context}
             }}
        """.format(file_name=calframe[1].filename.replace("\n", ""), locator=locator, context=calframe[1][4],
                   func_name=calframe[1][3])


