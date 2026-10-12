class Item:
    def __init__(self, product, quantity, price):
        self.quantity = quantity
        self.price = price

    def calculate_subtotal(self):
        return self.quantity * self.price

    def reserve_stock(self):
        pass
