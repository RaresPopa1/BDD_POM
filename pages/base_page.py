from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import unittest

class BasePage(Browser, unittest.TestCase):

    def wait_for_elem(self, xpath_selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_selector)))
        #PENTRU CA NU ERAU NISTE PARANTEZE         nu mergea                       ^                        ^

    def browser_back(self):
        self.driver.back()

    def alert_ok(self):               # ASA SE TRATEAZA ALERTELE
        sleep(1)
        self.driver.switch_to.alert.accept()

    def refresh_page(self):          # ASA SE DA REFRESH
        self.driver.refresh()

# TOTUL INCEPE DIN PAGES si BASE_PAGE unde punem metodele comune ale paginilor.
# Fiecare pagina/terminatie din site "/books" are cate o CLASA care mosteneste din base_page