import string

class Item:
    pay_rate = 0.8 # The pay rate after 20% is zero
    def __init__(self, name: str, price: float, quantity: int) -> None:

        #Check for wrong data input
        assert price >= 0, f'{price} should not be less than zero'
        assert quantity >= 0, f'{quantity} should not be less than zero'

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> int:
        return self.price * self.quantity 
    
    def apply_discount(self):
        self.price *= self.pay_rate



if __name__=='__main__':
    item1 = Item('Phone', 100, 1)
    item2 = Item('Laptop', 345, 4)





