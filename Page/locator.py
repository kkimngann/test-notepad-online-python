# coding=utf-8
class Locator():

#---------------------------Home page---------------------------#
    btn_login_homepage = "//a[contains(text(),'Đăng nhập')]"
    btn_close_banner = "//div[@class='shopee-popup__close-btn']"

#--------------------------Login page---------------------------#
    txt_email = "//input[@name = 'loginKey']"
    txt_pass = "//input[@name = 'password']"
    btn_login = "//button[contains(text(),'Đăng nhập')]"
    message_error = "//div[contains(text(),'message')]"
