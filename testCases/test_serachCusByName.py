import time

import pytest

from pageObjects.Loginpage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchCustomerPage import Search_Customer
from pageObjects.AddCustomerPage import Addcustomer


class Test_SearchCustByname_004:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getuserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustByname(self, setup):
        self.logger.info("*************** Test_SearchCustByname_004 *************** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("*********** login into app ***********")
        self.lp = Loginpage(self.driver)
        self.lp.set_user_name(self.useremail)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("******** login success ************")

        self.logger.info("******* starting search customer by name ***********")
        self.ap = Addcustomer(self.driver)
        self.ap.clickcustomermenu()
        self.ap.clickcustomerMenuitemtem()

        self.sc = Search_Customer(self.driver)
        self.sc.setfstname("Victoria")
        self.sc.setlstname("Terces")
        self.sc.clickbtn_search()
        time.sleep(3)
        status = self.sc.search_cus_byName("Victoria Terces")
        if status == True:
            assert True
            self.logger.info("*************** Test_SearchCustByname_004 Passed *************** ")
        else:
            self.logger.info("*************** Test_SearchCustByname_004 Finished *************** ")
            assert False

        self.logger.info("*************** Test_SearchCustByname_004 Finished *************** ")

        self.driver.close()
