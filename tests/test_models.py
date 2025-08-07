import pytest
from models import Product
from tests.factories import fake_product

@pytest.fixture
def sample_product():
    product = fake_product()
    product.save()  
    return product

def test_read_product(sample_product):
    fetched = Product.find_by_id(sample_product.id)
    assert fetched is not None
    assert fetched.name == sample_product.name

def test_update_product(sample_product):
    new_name = "UpdatedName"
    sample_product.name = new_name
    sample_product.save()
    updated = Product.find_by_id(sample_product.id)
    assert updated.name == new_name

def test_delete_product(sample_product):
    product_id = sample_product.id
    sample_product.delete()
    deleted = Product.find_by_id(product_id)
    assert deleted is None

def test_list_all_products():
    products = Product.list_all()
    assert isinstance(products, list)

def test_find_by_name(sample_product):
    found = Product.find_by_name(sample_product.name)
    assert any(p.id == sample_product.id for p in found)

def test_find_by_category(sample_product):
    found = Product.find_by_category(sample_product.category)
    assert any(p.id == sample_product.id for p in found)

def test_find_by_availability():
    available_products = Product.find_by_availability(True)
    for product in available_products:
        assert product.available is True
