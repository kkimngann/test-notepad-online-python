#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Browser.browser import Browser
from Page.Page.homepage import HomePage
from Page.Page.loginpage import LoginPage
from pytest_bdd import scenarios, given, when, then
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('auto_test.cfg')


URL = config.get('URL', 'url')
BROWSER_NAME = config.get('BROWSER','browser')
# Scenarios
scenarios('../Feature/login.feature')

def setup():
    print('----------------------START TEST-------------------------')
    global obj_browser
    obj_browser = Browser(BROWSER_NAME)
    global login_page
    login_page = LoginPage(obj_browser)
    global home_page
    home_page = HomePage(obj_browser)



def teardown():
    print('------------------------END TEST-------------------------')
    obj_browser.browser.quit()

@given('Access Shopee website')
def function_given():
    obj_browser.browser.get(URL)


@given('Choose Register')
def choose_login():
    home_page.choose_btn_register()

@given('Close home banner (if any)')
def close_banner():
    home_page.close_banner()

@when('Input email <email>')
def input_phone(email):
    login_page.input_email(email)

@when('Input password <password>')
def input_pass(password):
    login_page.input_password(password)

@when('Choose button Login')
def choose_btn_login():
    login_page.choose_btn_login()

@then('Show error <message> correct')
def check_message(message):
    actual = login_page.get_error_message(message)
    assert message == actual

@then('Verify button login is disable')
def check_login_disabled():
    assert login_page.is_disabled_button_login()



