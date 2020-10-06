import abc


class Beverage():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def cost(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass


class AddOn():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def cost(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass


class Expresso(Beverage):
    def cost(self):
        return 2

    def get_description(self):
        return "Expresso"


class Mocha(Beverage):
    def cost(self):
        return 5

    def get_description(self):
        return "Mocha"


def Latte(Beverage):
    def cost(self):
        return 3

    def get_description(self):
        return "Latte"


class CaramelAddOn(AddOn):
    _beverage = None

    def __init__(self, beverage):
        self._beverage = beverage

    def cost(self):
        return self._beverage.cost() + 2

    def get_description(self):
        return self._beverage.get_description() + ", Caramel"


class ChocoletAddOn(AddOn):
    _beverage = None

    def __init__(self, beverage):
        self._beverage = beverage

    def cost(self):
        return self._beverage.cost() + 4

    def get_description(self):
        return self._beverage.get_description() + ", Chocolate"


my_coffee = Expresso()
my_coffee = CaramelAddOn(my_coffee)

print("Coffee: %s, price: %s" %
      (my_coffee.get_description(), my_coffee.cost()))

my_coffee = ChocoletAddOn(my_coffee)

print("Coffee: %s, price: %s" %
      (my_coffee.get_description(), my_coffee.cost()))
