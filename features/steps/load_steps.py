from behave import given
from tests.factories import fake_product

@given('the following products exist')
def step_impl(context):
    context.products = []
    for row in context.table:
        product = fake_product()
        product.name = row['name']
        product.category = row['category']
        product.price = float(row['price'])
        product.available = row['available'].lower() == 'true'
        product.save()
        context.products.append(product)
