from behave import given, when, then
import requests

@given('I visit the index page')
def visit_index_page(context):
    context.response = requests.get('http://127.0.0.1:5000/')

@then('I should see an input field with the name "{field_name}"')
def check_input_field(context, field_name):
    assert field_name in context.response.text

@when('I submit valid input "{input_text}" in the input field')
def submit_valid_input(context, input_text):
    context.response = requests.post('http://127.0.0.1:5000/', data={'name': input_text})

@then('I should see the heading "{expected_heading}"')
def check_heading(context, expected_heading):
    assert expected_heading in context.response.text

@then('I should see the submitted input "{submitted_input}" displayed on the page')
def check_submitted_input(context, submitted_input):
    assert submitted_input in context.response.text

