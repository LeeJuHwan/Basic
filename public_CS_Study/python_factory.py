from abc import ABCMeta, abstractmethod


class Coffee(metaclass=ABCMeta):
    @abstractmethod
    def do_something(self):
        pass


class Latte(Coffee):
    def do_something(self):
        print("This is latte, do something more")


class Americano(Coffee):
    def do_something(self):
        print("This is americano, do something more")


class CoffeeFactory:
    def do_it(self, object_type):
        return eval(object_type.capitalize())().do_something()


coffee = input("what is your favorite coffee? Latte? Americano? ")
factory = CoffeeFactory()
factory.do_it(coffee)
