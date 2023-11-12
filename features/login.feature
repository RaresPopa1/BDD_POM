Feature: Login capability
#deoarece avem parti comune in fiecare scenariu, vom facem o parte 'background' care se ruleaza inainte de fiecare scenariu

  Background:
    Given home: I am a user on home page
    When home: I click bookstore application card
    When books: I click login button

#  @login
#  Scenario: I login with invalid credentials
#    When login: I login with user "rarespopa" and pass "Test123"
#    Then login: I validate that error message is displayed

  #Ok dar poate vrem sa facem mai multe scenarii dar nu vrem sa scriem aceleasi @

  @smoke
  Scenario: I login with valid credentials
    When login: I login with user "rarespopa" and pass "Test123!"
    Then books: I should land on books page

  @regression
  Scenario Outline: I login with invalid credentials
    When login: I login with user "<user>" and pass "<pswd>"
    Then login: I validate that error message is displayed

  Examples:
    | user      | pswd |
    | rarespopa | Test123 |
    | rarespopa | Test1234  |

### behave -f html -o behave-report_teste_.html --tags=regression