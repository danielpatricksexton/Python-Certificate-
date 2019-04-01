
class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings


    def scoops(self):
        list = []
        for i in self.ingredients:
            for t in self.toppings:
                list.append([i, t])
        return list


machine = IceCreamMachine(['vanilla', 'chocolate'], ['chocolate sauce'])
print(machine.scoops())
