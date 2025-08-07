import json
import pytest
from app import app  

@pytest.fixture
def client():
    return app.test_client()

def test_read_route(client, sample_product):
    response = client.get(f"/products/{sample_product.id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == sample_product.name

def test_update_route(client, sample_product):
    updated_data = {"name": "NewProductName"}
    response = client.put(f"/products/{sample_product.id}", json=updated_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == "NewProductName"

def test_delete_route(client, sample_product):
    response = client.delete(f"/products/{sample_product.id}")
    assert response.status_code == 204

def test_list_all_route(client):
    response = client.get("/products")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_list_by_name_route(client, sample_product):
    response = client.get(f"/products?name={sample_product.name}")
    assert response.status_code == 200
    data = response.get_json()
    assert any(p['id'] == sample_product.id for p in data)

def test_list_by_category_route(client, sample_product):
    response = client.get(f"/products?category={sample_product.category}")
    assert response.status_code == 200
    data = response.get_json()
    assert any(p['id'] == sample_product.id for p in data)

def test_list_by_availability_route(client):
    response = client.get("/products?available=true")
    assert response.status_code == 200
    data = response.get_json()
    for p in data:
        assert p['available'] is True
