import inspect
import os
import sys
from importlib import import_module
from importlib._bootstrap_external import SourceFileLoader
from os import listdir
from os.path import isfile, join

from mytestlib.base_page import BasePage


class BaseFactory:

    @staticmethod
    def init_pages(driver):
        path = os.path.dirname(os.path.abspath(__file__))
        modules = [module for module in listdir(path) if isfile(join(path, module))]
        pages = {}
        for module in modules:
            mod = SourceFileLoader(module.split('.py')[0], join(path, module)).load_module()

            for cl in dir(mod):
                obj = getattr(mod, cl)
                if inspect.isclass(obj) and issubclass(obj, BasePage) and obj is not BasePage:
                    pages[cl] = obj(driver)
        return pages





