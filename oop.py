class Item:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity



if __name__=='__main__':
    first_item = Item("Iphone", 1000, 5)
    print(first_item.calculate_total_price())

    second_item = Item("Redmi", 3909, 7)
    print(second_item.calculate_total_price())

 