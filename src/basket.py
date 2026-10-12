class Basket:

    def __init__(self, items):
        self.items = items

    def calculate_order_total(self):
        return sum(item.quantity * item.price for item in self.items)
