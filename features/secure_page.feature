Feature: Check functionality
  Scenario: Logout successfully
    Given Secure_page: I am on secure_page
    When Secure_page: I click logout_button
    Then Login_page: I return to login_page