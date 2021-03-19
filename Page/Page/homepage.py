#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.locator import Locator
class HomePage():
    def __init__(self,browser):
        self.browser = browser


    def choose_btn_more_menu(self):
        element = self.browser.find_element(Locator.btn_more_menu)
        self.browser.click_element(element,2)
        return True

    def choose_btn_login_register(self):
        element = self.browser.find_element(Locator.btn_login_register)
        self.browser.click_element(element,2)
        return True

    def check_login_success(self):
        element_logout = self.browser.find_element(Locator.menu_logout)
        element_setting = self.browser.find_element(Locator.menu_setting)
        return (element_setting is not False) and (element_logout is not False)
