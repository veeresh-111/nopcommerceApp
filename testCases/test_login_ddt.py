import time

import pytest

from pageObjects.Loginpage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test002_DDT_login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/loginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*****************Test002_DDT_login**************** ")
        self.logger.info("****************verifying Login DDT Test*************** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("number of rows in a excel sheet:", self.rows)

        lst_status = []  # impty list

        for r in range(2, self.rows+1):
            self.useremail = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.set_user_name(self.useremail)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'pass':
                    self.logger.info("***********passed************* ")
                    self.lp.click_logout()
                    lst_status.append('pass')
                elif self.exp == 'fail':
                    self.logger.info("***********failed************* ")
                    self.lp.click_logout()
                    lst_status.append('fail')
            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("***********failed************* ")
                    self.lp.click_logout()
                    lst_status.append('fail')
                elif self.exp == 'fail':
                    self.logger.info("***********passed************* ")
                    # self.lp.click_logout()
                    lst_status.append('pass')
            time.sleep(5)

        if 'fail' not in lst_status:
            self.logger.info("***********login DDT Test is passed************* ")
            self.driver.close()
            assert True
        else:
            self.logger.info("***********login DDT Test is failed************* ")
            self.driver.close()
            assert False

        self.logger.info("******** end of login DDT test**********")
        self.logger.info("********* completed Test002_DDT_login********")
