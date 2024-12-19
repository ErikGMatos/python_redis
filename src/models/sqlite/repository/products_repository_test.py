import pytest

from src.models.sqlite.repository.products_repository import ProductsRepository
from src.models.sqlite.settings.connection import SqliteConnectionHandler

conn_handle = SqliteConnectionHandler()
conn = conn_handle.connect()


@pytest.mark.skip(reason="Interaction with database")
def test_insert_product():
    repo = ProductsRepository(conn)
    name = "Joao"
    price = 10.0
    quantity = 10
    repo.insert_product(name, price, quantity)
    response = repo.find_product_by_name(name)
    print(response)


@pytest.mark.skip(reason="Interaction with database")
def test_find_product():
    repo = ProductsRepository(conn)
    name = "Joao"
    response = repo.find_product_by_name(name)
    print(response)
    print(type(response))
