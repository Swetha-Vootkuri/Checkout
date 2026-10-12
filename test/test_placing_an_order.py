import unittest
from unittest.mock import Mock

from src.basket import Basket
from src.order import Order


class TestPlacingOrder(unittest.TestCase):
    def test_basket_told_to_calculate_order_total(self):
        mock_basket = Basket()
        mock_basket.calculate_order_total = Mock()
        order = Order(mock_basket)
        order.place_order()
        mock_basket.calculate_order_total.assert_called_once()


