from pages.profile_page import ProfilePage
from behave import *

profile_page=ProfilePage() #facem un obiect ca sa gasim pasii

@when('profile: I remove the book with "{title}" from collection')
def step_impl(context, title):
    profile_page.click_delete_by_book_title(title)
    profile_page.click_confirm_delete_button()
    profile_page.alert_ok()

@then('profile: Book with "{title}" is present in collection')
def step_impl(context, title):
    profile_page.validate_book_displayed(title)

@then('profile: Book with "{title}" is NOT present in collection')
def step_impl(context, title):
    profile_page.validate_book_not_displayed(title)