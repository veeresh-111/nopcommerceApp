import pytest

from pageObjects.Loginpage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test001login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getuserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.logger.info("************Test001login************* ")
        self.logger.info("*************verifying Home page title*********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************Home page title test passed**************** ")

        else:
            self.driver.save_screenshot(".\\ScreenShots\\"+"test_homepage_title.png")
            self.driver.close()
            self.logger.error("***************Home page title test failed**************** ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****************verifying Login Test*************** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.set_user_name(self.useremail)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.lp.click_logout()
            self.driver.close()
            self.logger.info("***********login Test passed************* ")

        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("**************Login Test failed************** ")
            assert False
