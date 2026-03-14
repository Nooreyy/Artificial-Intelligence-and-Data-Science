'''A food delivery application supports multiple restaurants.

Create a base class called:
Restaurant
with a method:
prepare_food()
Create three child classes that override this method:

PizzaRestaurant
BurgerRestaurant
ChineseRestaurant
Each class should print a different food preparation message.

Example:
Preparing Pizza
Preparing Burger
Preparing Noodles
Create objects of all classes and call the prepare_food() method.
Bonus Question (Optional – Advanced Logic)
'''

class Restaurant:
    def prepare_food(self):
        pass

class PizzaRestaurant(Restaurant):
    def prepare_food(self):
        print("Preparing Pizza")
class BurgerRestaurant(Restaurant):
    def prepare_food(self):
        print("Preparing Burger")
class ChineseRestaurant(Restaurant):
    def prepare_food(self):
        print("Preparing Noodles")

# Create objects of all classes and call the prepare_food() method
pizza_restaurant = PizzaRestaurant()
burger_restaurant = BurgerRestaurant()
chinese_restaurant = ChineseRestaurant()
pizza_restaurant.prepare_food()
burger_restaurant.prepare_food()
chinese_restaurant.prepare_food()
