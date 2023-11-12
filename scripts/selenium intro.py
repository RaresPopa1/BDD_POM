# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome (sau cum vrem sa l definim)
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url # inspect ctrlF scriem '//input[@id="username"]'
chrome.get('https://the-internet.herokuapp.com/login')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(2)

# completam username in f de atribut=valoare SI PAROLA
chrome.find_element(By.XPATH, '//input[@id="username"]').send_keys('tomsmith')
sleep(2)

#completam parola in f de atribut=valoare
chrome.find_element(By.XPATH, '//input[@id="password"]').send_keys('SuperSecretPassword!')
sleep(2)

#dam click pe login #//*[text()=" Login"]
#in f de text
chrome.find_element(By.XPATH, '//*[text()=" Login"]').click()
sleep(4)
#alta varianta de copiere cale, click dreapta in chrome in cod, COPY>XPATH //*[@id="password"]

#verificam ca am ajuns pe pagina corecta
expected='https://the-internet.herokuapp.com/secure'
actual= chrome.current_url
assert expected==actual, "Incorrect URL"

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')