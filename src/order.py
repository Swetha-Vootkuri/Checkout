class Order:
    def __init__ (self,basket):
        self.basket = basket

    def place_order(self):
        self.basket.calculate_order_total()
