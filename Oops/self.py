class Market:
    
    def buyVegetables(self):
        self.name = "Tomato"
        self.price = 40


    
s1 = Market()
s2 = Market()

s1.name = "Cucumber"
s1.price = 56

s2.name = "Carrots"
s2.price = 57


print(s2.__dict__)
Market.buyVegetables(s1)