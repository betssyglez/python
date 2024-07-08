class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water: {self.resources['water']} ml")
        print(f"Milk: {self.resources['milk']} ml")
        print(f"Coffee: {self.resources['coffee']} g")

    def enough_source(self, drink):
        make_it = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}")
                make_it = False
        return make_it

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}. Enjoy it!")
