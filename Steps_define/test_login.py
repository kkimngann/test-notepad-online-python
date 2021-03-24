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



def teardown():
    print('------------------------END TEST-------------------------')
    obj_browser.browser.quit()

@given('Access online notepad website')
def function_given():
    obj_browser.browser.get(URL)


@given('Choose Register/Login')
def choose_login():
    page = HomePage(obj_browser)
    page.choose_btn_login_register()

@when('Input email <email>')
def input_phone(email):
    page = LoginPage(obj_browser)
    page.input_email(email)

@when('Input password <password>')
def input_pass(password):
    page = LoginPage(obj_browser)
    page.input_password(password)

@when('Choose button Login')
def choose_btn_login():
    page = LoginPage(obj_browser)
    page.choose_btn_login()

@then('Show error <message> correct')
def check_message(message):
    page = LoginPage(obj_browser)
    expected = message
    actual = page.get_error_message()
    assert expected == actual

@then('Login successful and show list menu correct')
def check_login_success():
    page = HomePage(obj_browser)
    assert page.check_login_success()


