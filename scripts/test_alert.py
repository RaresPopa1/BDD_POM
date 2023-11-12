from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()

chrome.maximize_window()

chrome.get('https://demoqa.com/alerts')
sleep(3)

chrome.find_element(By.ID, 'alertButton').click() # ALTA METODA DE A GASI ELEMENTE
sleep(3)

chrome.switch_to.alert.accept()
sleep(3)

chrome.quit()

print('SUCCESS - TEST PASSED')