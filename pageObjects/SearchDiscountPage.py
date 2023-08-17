from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Search_DiscountPage:
    lnkpromotion_xpath = "//p[normalize-space()='Promotions']"
    lnkDiscounts_xpath = "//p[normalize-space()='Discounts']"
    discountName_xpath = "//input[@id='SearchDiscountName']"
    strdate_xpath = "//input[@id='SearchStartDate']"
    enddate_xpath = "//input[@id='SearchEndDate']"
    drp_discountType_xpath = "//select[@id='SearchDiscountTypeId']"
    btndissearch_xpath = "//button[@id='search-discounts']"

    searchresult_xpath = "//div[@id='discounts-grid_wrapper']"
    table_xpath = "//table[@id='discounts-grid']"
    tablerow_xpath = "//table[@id='discounts-grid']/tbody/tr"
    tablecolumn_xpath = "//table[@id='discounts-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def clicklnkpromotion(self):
        self.driver.find_element(By.XPATH, self.lnkpromotion_xpath).click()

    def clicklnkdiscount(self):
        self.driver.find_element(By.XPATH, self.lnkDiscounts_xpath).click()

    def setdiscountName(self, Name):
        self.driver.find_element(By.XPATH, self.discountName_xpath).send_keys(Name)

    def setstrdate(self, strdate):
        self.driver.find_element(By.XPATH, self.strdate_xpath).send_keys(strdate)

    def setenddate(self, enddate):
        self.driver.find_element(By.XPATH, self.enddate_xpath).send_keys(enddate)

    def setdiscountType(self, disctype):
        drp_disctype = Select(self.driver.find_element(By.XPATH, self.drp_discountType_xpath))
        drp_disctype.select_by_visible_text(disctype)

    def clickDiscsearchbtn(self):
        self.driver.find_element(By.XPATH, self.btndissearch_xpath).click()

    def getrowcount(self):
        return len(self.driver.find_elements(By.XPATH, self.tablerow_xpath))

    def getcolumncount(self):
        return len(self.driver.find_elements(By.XPATH, self.tablecolumn_xpath))

    def search_discountByName(self, discount):
        flag = False
        for r in range(1, self.getrowcount() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            discout_result = table.find_element(By.XPATH,
                                                "//table[@id='discounts-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if discout_result == discount:
                flag = True
                break

        return flag
