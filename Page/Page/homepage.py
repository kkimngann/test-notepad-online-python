#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.locator import Locator
class HomePage():
    def __init__(self,browser):
        self.browser = browser


    def choose_btn_register(self):
        element = self.browser.find_element(Locator.btn_login_homepage)
        self.browser.click_element(element,2)
        return True
    def close_banner(self):
        element = self.browser.find_element(Locator.btn_close_banner)
        if element is not False:
            self.browser.click_element(element, 2)
        return True
