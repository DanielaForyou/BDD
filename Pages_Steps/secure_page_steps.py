from behave import *


@given('Secure_page: I am on secure_page')
def impl_step(context):
    context.secure_page_object.navigate_to_secure_page()

@when('Secure_page: I click logout_button')
def impl_step(context):
    context.secure_page_object.click_logout_button()

@then('Login_page: I return to login_page')
def impl_step(context):
    context.login_page_object.verify_if_login_button_is_displayed()