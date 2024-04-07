from datetime import date
class Market:
    __name=  "Kartik"
    def __init__(self,name,age, price):
        self.name = name
        self.age = age
        self.price = price

    
    # let discuss about the class method

    @classmethod
    def ageCalculator(cls, name, year, price):
         return cls(name,date.today().year - year, price)
    
    def customerDetails(self):
        print("Name = ",self.name)
        print("Age = ",self.age)
        print("Price = ",self.price)

s1 = Market("kartik", 21, 45000)
print(Market._Market__name) # way to access the private class or variable
s1 = Market.ageCalculator("Nitin", 23, 60420)
s1.customerDetails()