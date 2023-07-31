import time

from selenium.webdriver.common.by import By


class Loginpage:

    textbox_username_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self, useremail):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(useremail)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
