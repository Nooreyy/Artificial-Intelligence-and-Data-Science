'''An online shopping system wants to manage a customer's cart.
Create a class called:
ShoppingCart
The class should include methods:
add_item(name, price)
remove_item(name)
show_total()
The cart should store multiple items and calculate the total price'''

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, name, price):
        self.cart[name] = price
        print(f"Added {name} to cart at ${price}.")

    def remove_item(self, name):
        if name in self.cart:
            del self.cart[name]
            print(f"Removed {name} from cart.")
        else:
            print(f"{name} not found in cart.")

    def show_total(self):
        total = sum(self.cart.values())
        print(f"Total price of items in cart: ${total}")

# Example usage
cart = ShoppingCart()
cart.add_item("Laptop", 999)
cart.add_item("Headphones", 199)
cart.show_total()
cart.remove_item("Headphones")
cart.show_total()
