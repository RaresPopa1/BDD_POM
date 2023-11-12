from selenium import webdriver

class Browser():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()

    def close(self):
        self.driver.quit() #deoarece ramanem logati si da fail testul de dubla logare, o sa punem in loc de.close .quit