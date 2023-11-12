from pages.books_page import BooksPage
from behave import *
from time import sleep

books_page=BooksPage() #facem un obiect ca sa gasim pasii

@when('books: I click login button')
def step_impl(context):
    books_page.click_login_button()

@then('books: I should land on books page')
def step_impl(context):
    books_page.validate_correct_url()

@then('books: I validate that 8 books are displayed')
def step_impl(context):
    books_page.validate_books_count(8)


@when('books: I search after "{query}"')
def step_impl(context, query):
    books_page.fill_search_input(query)

@when('books: I add to collection the book with title "{title}"')
def step_impl(context, title):
    books_page.click_book_by_title(title)
    books_page.click_add_to_your_collection_button()
    books_page.browser_back()
    sleep(1) # se grabeste si sare pasi

@then('books: I validate that only "{title}" book is displayed')
def step_impl(context, title):
    books_page.validate_books_count(1)
    books_page.validate_books_title(title)

@when('books: I clear search input')
def step_impl(context):
    books_page.clear_search_input()

# Al doilea pas STEPS
# Cu sintaxa Gherkin - Given When Then

# Al 3-lea pas .feature. unde expunem in limba engleza ce face.


