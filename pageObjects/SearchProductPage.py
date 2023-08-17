from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Searchproductpage:

    lnkcatalog_xpath = "//p[normalize-space()='Catalog']"
    lnkproduct_xpath = "//p[normalize-space()='Products']"
    txtfldproductName_xpath = "//input[@id='SearchProductName']"
    drpCategory_xpath = "//select[@id='SearchCategoryId']"
    drpmanufacturer_xpath = "//select[@id='SearchManufacturerId']"
    drpvendor_xpath = "//select[@id='SearchVendorId']"
    drpwarehouse_xpath = "//select[@id='SearchWarehouseId']"
    drpproducttype_xpath = "//select[@id='SearchProductTypeId']"
    drppublised_xpath = "//select[@id='SearchPublishedId']"
    btnsearchproduct_xpath = "//button[@id='search-products']"
    searchresult_xpath = "//div[@id='products-grid_wrapper']"
    table_xpath = "//table[@id='products-grid']"
    tablerows_xpath = "//table[@id='products-grid']/tbody/tr"
    tablecolumns_xpath = "//table[@id='products-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def clicklnkcatalog(self):
        self.driver.find_element(By.XPATH, self.lnkcatalog_xpath).click()
    def clicklnkproduct(self):
        self.driver.find_element(By.XPATH, self.lnkproduct_xpath).click()
    def settxtfldproductname(self, proName):
        self.driver.find_element(By.XPATH, self.txtfldproductName_xpath).send_keys(proName)
    def setdrpcategory(self, category):
        drpcategory = Select(self.driver.find_element(By.XPATH, self.drpCategory_xpath))
        drpcategory.select_by_visible_text(category)
    def setdrpmanufacturer(self, manufacturer):
        drpmanufacturer = Select(self.driver.find_element(By.XPATH, self.drpmanufacturer_xpath))
        drpmanufacturer.select_by_visible_text(manufacturer)
    def setdrpvendor(self, vendor):
        drpvendor = Select(self.driver.find_element(By.XPATH, self.drpvendor_xpath))
        drpvendor.select_by_visible_text(vendor)
    def setdrpwarehouse(self, warehouse):
        drpwarehouse = Select(self.driver.find_element(By.XPATH, self.drpwarehouse_xpath))
        drpwarehouse.select_by_visible_text(warehouse)
    def setdrpproducttype(self, producttype):
        drpproducttype = Select(self.driver.find_element(By.XPATH, self.drpproducttype_xpath))
        drpproducttype.select_by_visible_text(producttype)
    def setdrppublised(self, publised):
        drppublised = Select(self.driver.find_element(By.XPATH, self.drppublised_xpath))
        drppublised.select_by_visible_text(publised)
    def clickbtnsearchproduct(self):
        self.driver.find_element(By.XPATH, self.btnsearchproduct_xpath).click()
    def getrowscount(self):
        return len(self.driver.find_elements(By.XPATH, self.tablerows_xpath))
    def getcolumnncount(self):
        return len(self.driver.find_elements(By.XPATH, self.tablecolumns_xpath))

    def searchproduct(self, ExpproductSKU):
        flag = False
        for r in range(1, self.getrowscount()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            ActproductSKU = table.find_element(By.XPATH, "//table[@id='products-grid']/tbody/tr["+str(r)+"]/td[4]").text
            if ActproductSKU == ExpproductSKU:
                flag = True
                break
            else:
                flag = False

        return flag
