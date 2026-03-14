'''A mobile shop wants to store information about mobile phones.

Create a class called Mobile with the following attributes:

Brand
Model
Price
Create two objects of the class and display their details using print statements.'''

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
# Create two objects of the Mobile class
mobile1 = Mobile("Apple", "iPhone 13", 999)
mobile2 = Mobile("Samsung", "Galaxy S21", 799)
# Display the details of the mobile phones
print(f"Mobile 1: \nBrand: {mobile1.brand}, Model: {mobile1.model}, Price: ${mobile1.price}")
print(f"Mobile 2: \nBrand: {mobile2.brand}, Model: {mobile2.model}, Price: ${mobile2.price}")
