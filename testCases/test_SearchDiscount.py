import pytest
import time

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.Loginpage import Loginpage
from pageObjects.SearchDiscountPage import Search_DiscountPage



class Test_search_discount_005:
    baseUrl = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getuserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_searchdiscount(self, setup):
        self.logger.info("************** Test_search_discount_005 **************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("*********** login into app ***********")
        self.lp = Loginpage(self.driver)
        self.lp.set_user_name(self.useremail)
        self.lp.set_password(self.password)
        self.lp.click_login()
        time.sleep(5)
        self.logger.info("******** login success ************")

        self.logger.info("************ stating search discount by name************")
        self.sd = Search_DiscountPage(self.driver)
        self.sd.clicklnkpromotion()
        self.sd.clicklnkdiscount()
        time.sleep(3)

        self.sd.setdiscountName("'20% order total' discount")
        # self.sd.setstrdate("01/01/2010")
        # self.sd.setenddate("01/01/2020")
        self.sd.setdiscountType("Assigned to order total")
        self.sd.clickDiscsearchbtn()
        time.sleep(5)

        status = self.sd.search_discountByName("20%")
        if status == True:
            assert True
            self.logger.info("*************** Test_search_discount_005 Passed *************** ")
        else:
            self.logger.info("*************** Test_search_discount_005 Failed*************** ")
            assert False

        self.logger.info("*************** Test_search_discount_005 Finished *************** ")

        self.driver.close()
