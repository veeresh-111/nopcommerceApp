from pageObjects.Loginpage import Loginpage
import pytest
import time
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.DashboardPage import Dashbord_page


class Personalstore001:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getuserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def personalstore(self, setup):
        self.logger.info("************login into application********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.set_user_name(self.useremail)
        self.lp.set_password(self.password)
        self.lp.click_login()

        time.sleep(3)
        self.logger.info("************ dashboard page**********")
        self.pp = Dashbord_page(self.driver)
        self.pp.clickplusbutton()
        time.sleep(3)
        self.pp.movetolink()


