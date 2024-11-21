from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_userid_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//button[@class='button-1 login-button']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element(By.ID,"textbox_userid_id").clear()
        self.driver.find_element(By.ID,"textbox_userid_id").send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.id,"textbox_password_id").clear()
        self.driver.find_element(By.ID,"textbox_password_id").send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,"button_login_xpath").click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,"link_logout_linktext").click()



