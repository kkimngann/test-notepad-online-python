#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
config = ConfigParser.RawConfigParser()
config.read('auto_test.cfg')

class Browser():
    def __init__(self,browser_name):
        self.browser_name = browser_name
        self.browser = self.open_browser()

    def open_browser(self):
        if self.browser_name == 'ie':
            browser_path = config.get("BROWSER PATH", "ie_path")
            browser = webdriver.Ie(executable_path=browser_path)
            time.sleep(5);
        elif self.browser_name == 'chrome':
            browser_path = config.get("BROWSER PATH", "chrome_path")
            print(browser_path)
            browser = webdriver.Chrome(browser_path)
        elif self.browser_name == 'firefox':
            browser_path = config.get("BROWSER PATH", "firefox_path")
            print(browser_path)
            browser = webdriver.Firefox(executable_path=browser_path)

        elif self.browser_name == 'edge':
            browser_path = config.get("BROWSER PATH", "edge_path")
            print(browser_path)
            browser = webdriver.Edge()
        else:
            browser_path = config.get("BROWSER PATH", "safari_path")
            print(browser_path)
            browser = webdriver.Safari(executable_path=browser_path)

        browser.implicitly_wait(5)
        browser.maximize_window()
        return browser

    def find_element(self, xpath_element):
        try:
            element = self.browser.find_element_by_xpath(xpath_element)
            return element
        except:
            return False

    def click_element(self, element, delay_time):
        try:
            element.click()
            time.sleep(delay_time)
        except:
            return False

    def set_text_element(self,element, text):
        try:
            element.send_keys(Keys.CONTROL + 'a')
            element.send_keys(Keys.DELETE)
            element.send_keys(text)
        except:
            return False

    def get_text_element(self, element):
        try:
            return element.text
        except:
            return ''
