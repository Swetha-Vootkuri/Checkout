class Basket:

    def __init__(self, items):
        self.items = items

    def calculate_order_total(self):
        return sum(item.calculate_subtotal() for item in self.items)
