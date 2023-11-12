from pages.left_menu import LeftMenu
from behave import *

left_menu=LeftMenu() #facem un obiect ca sa gasim pasii

@when('menu: I click profile_section')
def step_impl(context):
    left_menu.click_profile_section()
