from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
class LoginPage(BasePage):
    # selectors
    USER_INPUT = '//input[@id="userName"]'
    PASS_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//button[@id="login"]'
    INVALID_CREDENTIALS_ERROR = '//p[@id="name"]'

    # actions  #rarespoa Test123!
    def fill_user_input(self, user):
        self.wait_for_elem(self.USER_INPUT)
        self.driver.find_element(By.XPATH, self.USER_INPUT).send_keys(user)


    def fill_pass_input(self, pswd):
         self.wait_for_elem(self.PASS_INPUT)
         self.driver.find_element(By.XPATH, self.PASS_INPUT).send_keys(pswd)

    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    # Validare
    def validate_invalid_credentials_error(self):
        sleep(1) #pt ca se misca prea repede da eroare si tre sa ii dam putin timp de incarcare
        #sau self.wait_for_elem(self.INVALID_CREDENTIALS_ERROR)
        expected = 'Invalid username or password!'
        actual = self.driver.find_element(By.XPATH, self.INVALID_CREDENTIALS_ERROR).text
        self.assertEqual(expected, actual, 'Error Message is Incorrect')
