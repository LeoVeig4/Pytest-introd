from unittest.mock import Mock
from app.itemDatabase import ItemDatabase
from app.carrinho import Carrinho
import pytest


@pytest.fixture
def cart():
    # All setup for the cart here...
    return Carrinho(5)


def test_can_add_item_to_cart(cart):
    cart.add("maça")
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    cart.add("maça")
    assert "maça" in cart.get_items()


def test_when_add_more_than_max_items_should_fail(cart):
    for _ in range(5):
        cart.add("maça")

    with pytest.raises(OverflowError):
        cart.add("maça")


def test_can_get_total_price(cart):
    cart.add("maça")
    cart.add("laranja")
    item_database = ItemDatabase()

    def mock_get_item(item: str):
        if item == "maça":
            return 1.0
        if item == "laranja":
            return 2.0

    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 3.0
