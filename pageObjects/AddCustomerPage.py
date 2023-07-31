import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class Addcustomer:

    lnkCustomers_Menu = "//a[@href='#']/p[contains(text(),'Customers')]"
    lnkCustomers_MenuItem = "//a[@href='/Admin/Customer/List']/p[contains(text(),'Customers')]"
    btnAddNew = "//a[@href='/Admin/Customer/Create']"

    txtEmail = "//input[@id='Email']"
    txtPassword = "//input[@id='Password']"
    txtFirstName = "//input[@id='FirstName']"
    txtLastName = "//input[@id='LastName']"
    rdMaleGender = "Gender_Male"
    rdFemaleGender = "Gender_Female"
    txtDob = "//input[@id='DateOfBirth']"
    txtCompanyName = "//input[@id='Company']"
    txtCustomerRoles = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemAdmistrators = "//li[contains(text(),'Administrators')]"
    lstitemRegistered = "//li[contains(text(),'Registered')]"
    lstitemGuests = "//li[contains(text(),'Guests')]"
    lstitemVendors = "//li[contains(text(),'Vendors')]"
    drpMngofVendor = "//select[@id='VendorId']"
    txtAdminContent = "//textarea[@id='AdminComment']"
    btnSave = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickcustomermenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_Menu).click()

    def clickcustomerMenuitemtem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_MenuItem).click()

    def clickaddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddNew).click()

    def settxtemail(self, custemail):
        self.driver.find_element(By.XPATH, self.txtEmail).clear()
        self.driver.find_element(By.XPATH, self.txtEmail).send_keys(custemail)

    def settxtpassword(self, custpassword):
        self.driver.find_element(By.XPATH, self.txtPassword).clear()
        self.driver.find_element(By.XPATH, self.txtPassword).send_keys(custpassword)

    def settxtFirstname(self, fstname):
        self.driver.find_element(By.XPATH, self.txtFirstName).clear()
        self.driver.find_element(By.XPATH, self.txtFirstName).send_keys(fstname)

    def settxtLastname(self, lstname):
        self.driver.find_element(By.XPATH, self.txtLastName).clear()
        self.driver.find_element(By.XPATH, self.txtLastName).send_keys(lstname)

    def setrdgender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemaleGender).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender).click()

    def settxtdob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob).clear()
        self.driver.find_element(By.XPATH, self.txtDob).send_keys(dob)

    def settxtCompanyname(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName).clear()
        self.driver.find_element(By.XPATH, self.txtCompanyName).send_keys(comname)

    def settxtcustomerrole(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles).click()
        time.sleep(3)
        if role == 'Registered':
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered)
        elif role == 'Administrators':
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdmistrators)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests)
        elif role == 'Vendors':
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setdrpMngofvendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpMngofVendor))
        drp.select_by_visible_text(value)

    def settxtAdmincontent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent).clear()
        self.driver.find_element(By.XPATH, self.txtAdminContent).send_keys(content)

    def clickbtnsave(self):
        self.driver.find_element(By.XPATH, self.btnSave).click()
