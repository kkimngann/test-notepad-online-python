#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.locator import Locator
class LoginPage():
    def __init__(self,browser):
        self.browser = browser

    def input_email(self, text):
        element = self.browser.find_element(Locator.txt_email)
        self.browser.set_text_element(element, text)
        return True

    def input_password(self,text):
        element = self.browser.find_element(Locator.txt_pass)
        self.browser.set_text_element(element, text)
        return True

    def choose_btn_login(self):
        element = self.browser.find_element(Locator.btn_login)
        self.browser.click_element(element,2)
        return True

    def get_error_message(self,expected_message):
        element = self.browser.find_element(Locator.message_error.replace("message",expected_message))
        if element is not False:
            message = self.browser.get_text_element(element)
            return message
        else:
            return False

    def is_disabled_button_login(self):
        element = self.browser.find_element(Locator.btn_login)
        if element is not False:
            return not element.is_enabled()
        else:
            return False
