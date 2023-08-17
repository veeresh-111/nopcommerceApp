import time
import pytest


from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchProductPage import Searchproductpage
from pageObjects.Loginpage import Loginpage


class Test_searchproduct_006:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getuserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_searchproduct(self, setup):
        self.logger.info("***************** Test_searchproduct_006 **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("************** login into app*************")
        self.lp = Loginpage(self.driver)
        self.lp.set_user_name(self.useremail)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("******** login successful ****************")
        time.sleep(5)

        self.logger.info("**************** starting test_searchproduct **************")
        self.sd = Searchproductpage(self.driver)
        self.sd.clicklnkcatalog()
        self.sd.clicklnkproduct()
        self.sd.settxtfldproductname("Apple MacBook Pro 13-inch")
        self.sd.setdrpcategory("All")
        self.sd.setdrpmanufacturer("Apple")
        self.sd.setdrpvendor("All")
        self.sd.setdrpwarehouse("All")
        self.sd.setdrpproducttype("Simple")
        self.sd.setdrppublised("All")
        self.sd.clickbtnsearchproduct()
        time.sleep(5)

        status = self.sd.searchproduct("AP_MBP_13")
        if status == True:
            assert True
            print("Number of search result product displayed", self.sd.getrowscount())
            self.logger.info("******************* Test_searchproduct_006 Passed ******************")
        else:
            self.logger.info("************** Test_searchproduct_006 Failed **********************")
            assert False

        self.logger.info("********************* Test_searchproduct_006 Finised *******************")
        self.driver.close()
