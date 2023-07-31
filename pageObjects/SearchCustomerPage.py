from selenium.webdriver.common.by import By


class Search_Customer:
    txtEmail_xpath = "//input[@id='SearchEmail']"
    txtfstname_xpath = "//input[@id='SearchFirstName']"
    txtlstname_xpath = "//input[@id='SearchLastName']"
    btnsearchCus_xpath = "//button[@id='search-customers']"

    searchResult_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tablerow_xpath = "//table[@id='customers-grid']//tbody/tr"
    tablecolumn_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setemail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setfstname(self, fname):
        self.driver.find_element(By.XPATH, self.txtfstname_xpath).send_keys(fname)

    def setlstname(self, lname):
        self.driver.find_element(By.XPATH, self.txtlstname_xpath).send_keys(lname)

    def clickbtn_search(self):
        self.driver.find_element(By.XPATH, self.btnsearchCus_xpath).click()

    def getnoofrows(self):
        return len(self.driver.find_elements(By.XPATH, self.tablerow_xpath))

    def getnoofcolumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tablecolumn_xpath))

    def search_cus_byEmail(self, email):
        flag = False
        for r in range(1, self.getnoofrows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def search_cus_byName(self, name):
        flag = False
        for r in range(1, self.getnoofrows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name_text = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name_text == name:
                flag = True
                break
        return flag
