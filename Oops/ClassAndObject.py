class Market:
    # global value that every object will have
    item = 40


s1 = Market() # Object
s2 = Market() # Object

s2.item = "Potato"
print(s1.__dict__)


print(s1.item)