class Order:
    def __init__ (self,basket,card=None):
        self.basket = basket
        self.card = card

    def place_order(self):
        self.card.charge(self.basket.calculate_order_total())
        self.basket.reserve_items()

