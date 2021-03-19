class Locator():

#---------------------------Home page---------------------------#
    btn_login_register = "//span[contains(text(),'Register/Login')]"
    menu_logout = "//span[contains(text(),'Logout')]"
    menu_setting = "//span[contains(text(),'Setting')]"


#--------------------------Login page---------------------------#
    txt_email = "//input[@id='loginEmail']"
    txt_pass = "//input[@placeholder='Enter Password']"
    btn_login = "//button[contains(text(),'Login')]"
    message_error = '//strong'
