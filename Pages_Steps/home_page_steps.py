from behave import *


@given('Home_page: I am on homepage')
def step_impl(context):
    context.home_page_object.navigate_to_homepage()


@when('Home_page: I click on Form Authentication')
def step_impl(context):
    context.home_page_object.enter_form_auth_url()


@then('Login_page: I am on login page')
def step_impl(context):
    context.login_page_object.verify_if_login_button_is_displayed()
