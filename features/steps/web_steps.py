from behave import given, when, then
import requests

API_URL = "http://localhost:5000/products"

@when('I request the product with name "{name}"')
def step_request_product(context, name):
    response = requests.get(f"{API_URL}?name={name}")
    context.response = response

@then('I should receive the product details with name "{name}"')
def step_verify_product_name(context, name):
    data = context.response.json()
    assert any(p['name'] == name for p in data)

@when('I update the product "{name}" with new price {price:f}')
def step_update_product_price(context, name, price):
    response = requests.get(f"{API_URL}?name={name}")
    product = response.json()[0]
    product_id = product['id']
    update_response = requests.put(f"{API_URL}/{product_id}", json={"price": price})
    context.response = update_response

@then('the product "{name}" should have price {price:f}')
def step_verify_product_price(context, name, price):
    response = requests.get(f"{API_URL}?name={name}")
    product = response.json()[0]
    assert product['price'] == price

@when('I delete the product with name "{name}"')
def step_delete_product(context, name):
    response = requests.get(f"{API_URL}?name={name}")
    product = response.json()[0]
    product_id = product['id']
    delete_response = requests.delete(f"{API_URL}/{product_id}")
    context.response = delete_response

@then('the product "{name}" should not exist')
def step_verify_product_deleted(context, name):
    response = requests.get(f"{API_URL}?name={name}")
    data = response.json()
    assert not any(p['name'] == name for p in data)

@when('I request all products')
def step_request_all_products(context):
    response = requests.get(API_URL)
    context.response = response

@then('I should receive a list of all products')
def step_verify_list_all_products(context):
    data = context.response.json()
    assert isinstance(data, list)
    assert len(data) > 0

@when('I search products by name "{name}"')
def step_search_by_name(context, name):
    response = requests.get(f"{API_URL}?name={name}")
    context.response = response

@then('I should receive products with name "{name}"')
def step_verify_search_by_name(context, name):
    data = context.response.json()
    assert all(p['name'] == name for p in data)

@when('I search products by category "{category}"')
def step_search_by_category(context, category):
    response = requests.get(f"{API_URL}?category={category}")
    context.response = response

@then('I should receive products in category "{category}"')
def step_verify_search_by_category(context, category):
    data = context.response.json()
    assert all(p['category'] == category for p in data)

@when('I search products by availability "{available}"')
def step_search_by_availability(context, available):
    response = requests.get(f"{API_URL}?available={available}")
    context.response = response

@then('I should receive products where availability is {available}')
def step_verify_search_by_availability(context, available):
    expected = available.lower() == 'true'
    data = context.response.json()
    assert all(p['available'] == expected for p in data)
