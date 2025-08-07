from faker import Faker
from models import Product  

fake = Faker()

def fake_product():
    return Product(
        name=fake.word(),
        category=fake.word(),
        price=round(fake.random_number(digits=5) / 100, 2),
        available=fake.boolean(chance_of_getting_true=75)  
    )
