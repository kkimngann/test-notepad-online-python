#!/usr/bin/env python
# coding=utf-8
Feature Login
  As A user I want to login

  Background:
    Given Access Shopee website
    And Close home banner (if any)
    And Choose Register


  Scenario Outline: Verify that button Login is disable if not input username or/and password
    When Input email <email>
    And Input password <password>
    Then Verify button login is disable
    Examples:
    |email          |password|
    |               |        |
    | abc@gmail.com |        |
    |               |12345678|

  Scenario Outline: Verify that error message shown correctly if not input invalid login info
    When Input email <email>
    And Input password <password>
    And Choose button Login
    Then Show error <message> correct
    Examples:
    |email          |password   |message|
    | abc@@gmail.com | 12345678  |Đăng nhập KHÔNG thành công. Bạn vui lòng thử lại hoặc đăng nhập bằng cách khác nhé!|
    | abc@gmail.com |12345678|Tên tài khoản của bạn hoặc Mật khẩu không đúng, vui lòng thử lại                               |