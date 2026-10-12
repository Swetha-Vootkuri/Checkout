import unittest
from unittest.mock import Mock

from src.basket import Basket
from src.order import Order


class Item:
    def __init__(self, product, quantity, price):
        self.quantity = quantity
        self.price = price


class TestPlacingOrder(unittest.TestCase):
    def test_basket_told_to_calculate_order_total(self):
        mock_basket = Basket([])
        mock_basket.calculate_order_total = Mock()
        order = Order(mock_basket)
        order.place_order()
        mock_basket.calculate_order_total.assert_called_once()

    def test_calculate_basket_total(self):
        basket = Basket([Item("Bamboo socks", 2, 7.50), Item("Gift wrap", 1, 4.99)])
        self.assertAlmostEqual(19.99, basket.calculate_order_total())




