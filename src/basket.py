class Basket:

    def __init__(self, items,card=None):
        self.items = items


    def calculate_order_total(self):
        return round(sum(item.calculate_subtotal() for item in self.items), 2)
