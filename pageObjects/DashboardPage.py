
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Dashbord_page:

    button_plus_xpath = "//div[@id='configuration-steps-card']//i[@class='fas fa-plus']"
    link_personalstore_xpath = "//small[contains(text(),'Choose a beautiful theme for your store and add yo')]"

    def __init__(self, driver):
        self.driver = driver

    def clickplusbutton(self):
        self.driver.find_element(By.XPATH, self.button_plus_xpath).click()

    def movetolink(self):
        personal_link = self.driver.find_element(By.XPATH, self.link_personalstore_xpath)
        self.act = ActionChains()
        self.act.move_to_element(personal_link)



