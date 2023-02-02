class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: int) -> None:
        # Run validations to received arguments
        assert price >= 0, f"Price {price} can't be less than 0"
        assert quantity >= 0, f"Quantity {quantity} can't be less than 0"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate



if __name__=='__main__':
    first_phone = Item("Iphone", 1000, 5)
    second_phone = Item("Redmi", 3909, 7)
    third_phone = Item("Nokia", 4500, 2)
    fourth_phone = Item("Samsung", 5000, 4)
    fifth_phone = Item("Huwai", 4900, 9)

    for n in Item.all:
        print(f"{n.name} price is {n.price} and we have {n.quantity} in stock.")
 