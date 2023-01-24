from behave import *


@given('Login_page: I am on login_page')
def step_impl(context):
    context.login_page_object.navigate_to_login_page()

@when('Login_page: I introduce the right username: "{username}"')
def step_impl(context, username):
    context.login_page_object.introduce_user(username)

@when('Login_page: I introduce the right password: "{password}"')
def step_impl(context, password):
    context.login_page_object.introduce_password(password)

@when('Login_page: I introduce an invalid username: "{username}"')
def step_impl(context, username):
    context.login_page_object.introduce_user(username)

@when('Login_page: I introduce an invalid password: "{password}"')
def step_impl(context, password):
    context.login_page_object.introduce_password(password)

@when('Login_page: I click login_button')
def step_impl(context):
    context.login_page_object.click_login_button()

@then('Secure_page: I am on secure_page')
def step_impl(context):
    context.secure_page_object.verify_succes_message()

@then('Login_page: I get the message: "{expected}"')
def step_impl(context,expected):
    context.login_page_object.verify_text_message(expected)
