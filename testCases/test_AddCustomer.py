import random
import string

import pytest

from pageObjects.Loginpage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddCustomerPage import Addcustomer
from selenium.webdriver.common.by import By


class Test_003_Addcustomer:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getuserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self, setup):
        self.logger.info("*************** Test_003_Addcustomer *************** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("*********** login into app ***********")
        self.lp = Loginpage(self.driver)
        self.lp.set_user_name(self.useremail)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("******** login success ************")

        self.logger.info("*********** Starting add customer Test ***********")
        self.ap = Addcustomer(self.driver)
        self.ap.clickcustomermenu()
        self.ap.clickcustomerMenuitemtem()
        self.ap.clickaddnew()

        self.logger.info("********** adding customer details **********")
        self.email = random_generator() + "@gmail.com"
        self.ap.settxtemail(self.email)
        self.ap.settxtpassword('test123')
        self.ap.settxtFirstname('veeresh')
        self.ap.settxtLastname('sk')
        self.ap.setrdgender('Male')
        self.ap.settxtdob('1/06/1994')
        self.ap.settxtCompanyname('busyQA')
        self.ap.settxtcustomerrole('Guests')
        self.ap.setdrpMngofvendor('Vendor 2')
        self.ap.settxtAdmincontent('This is for testing.............')
        self.ap.clickbtnsave()

        self.logger.info("********* Saved customer details successfully*********")

        self.logger.info("*********** started validation **********")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("************ Add customer Test Passed**********")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_addcustomer_scr.png")
            self.logger.error("************ Add customer Test Failed **********")
            assert False

        self.driver.close()
        self.logger.info("********** ending add customer test**************")

@pytest.mark.sanity
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
