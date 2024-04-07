class Market:
    def __init__(self, item, price):
        self.item = item # s1.item = "Carrot" this is same
        self.price = price


# s1.item = "Carrot"

s1 = Market("Carrot", 34)

print(s1.__dict__)