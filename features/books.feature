Feature: Books capability

#Avantaj BDD - deja am refolosit 4 pasi din alt .feature

  Background:
    Given home: I am a user on home page
    When home: I click bookstore application card
    When books: I click login button
    When login: I login with user "rarespopa" and pass "Test123!"

  @regression
  Scenario: I validate the stock count
    Then books: I validate that 8 books are displayed

  @regression
  Scenario Outline: I validate the search is working
    When books: I search after "<querry>"
    Then books: I validate that only "Git Pocket Guide" book is displayed
  Examples:
    | querry  |
    | Git     |
    | Richard |

 @regression
  Scenario: I validate that clear search is working
    When books: I search after "test"
    When books: I clear search input
    Then books: I validate that 8 books are displayed

# behave -f html -o behave-report_teste_.html --tags=regression