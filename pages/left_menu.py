from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LeftMenu(BasePage):
    # selectors
    PROFILE_BUTTON = '//span[text()="Profile"]'

    # actions
    def click_profile_section(self):  #nu vrea si dam force click din javascript
        self.wait_for_elem(self.PROFILE_BUTTON)
        element = self.driver.find_element(By.XPATH, self.PROFILE_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)