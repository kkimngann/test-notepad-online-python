#!/usr/bin/env python
# -*- coding: utf-8 -*-
Feature Login
  As A user I want to login

  Background:
    Given Access online notepad website
    And Choose Register/Login

  Scenario Outline: Login unsuccessful with incorrect email and/or password
    When Input email <email>
    And Input password <password>
    And Choose button Login
    Then Show error <message> correct
    Examples:
    |email        |password|message|
    |abc@gmail.com|12345678|Email and password do not match|
    |abc@gmail.com|        |tbu|
    |             |12345678|tbu|

  Scenario Outline: Login successful with correct email and password
    When Input email <email>
    And Input password <password>
    And Choose button Login
    Then Login successful and show list menu correct
    Examples:
    |email              |password|
    |kkimngann@gmail.com|12345|