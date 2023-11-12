from pages.login_page import LoginPage
from behave import * #all

login_page = LoginPage() #facem un obiect ca sa gasim pasii

@when('login: I login with user "{user}" and pass "{pswd}"')
def step_impl(context, user, pswd):
    login_page.fill_user_input(user)
    login_page.fill_pass_input(pswd)
    login_page.click_login_button()

#@when('login: I login with invalid credentials')
#def step_impl(context):
#    login_page.fill_user_input('rarespopa')
#    login_page.fill_pass_input('Test123')
#    login_page.click_login_button()

@then('login: I validate that error message is displayed')
def step_impl(context):
    login_page.validate_invalid_credentials_error()

