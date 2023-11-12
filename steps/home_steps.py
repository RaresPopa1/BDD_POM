from pages.home_page import HomePage
from behave import *

#sintaxa Gherkin
#given - selecteaza situatia ititiala
#when - actiunile intermediare
#then - verificare finala

home_page = HomePage ()
@given('home: I am a user on home page')
def step_impl(context):
    home_page.driver.delete_all_cookies() #FOARTE UTIL -! ca sa nu ramanem logati, vom putea astfel sa facem login valid primul.
    home_page.navigate_to_home_page()

@when('home: I click bookstore application card')
def step_impl(context):
    home_page.click_book_store_application_card()


