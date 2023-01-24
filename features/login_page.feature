Feature: Test Functionality
  Background:
    Given Login_page: I am on login_page

  Scenario: Log in successfully
    When Login_page: I introduce the right username: "tomsmith"
    When Login_page: I introduce the right password: "SuperSecretPassword!"
    When Login_page: I click login_button
    Then Secure_page: I am on secure_page


  Scenario: Log in with invalid username
    When Login_page: I introduce an invalid username: "hello"
    When Login_page: I introduce the right password: "SuperSecretPassword!"
    When Login_page: I click login_button
    Then Login_page: I get the message: "Your username is invalid!"


  Scenario: Log in with invalid password
    When Login_page: I introduce the right username: "tomsmith"
    When Login_page: I introduce an invalid password: "helloWorld"
    When Login_page: I click login_button
    Then Login_page: I get the message: "Your password is invalid!"


  Scenario: Log in with invalid password and username
    When Login_page: I introduce an invalid username: "hello"
    When Login_page: I introduce an invalid password: "helloWorld"
    When Login_page: I click login_button
    Then Login_page: I get the message: "Your username is invalid!"




