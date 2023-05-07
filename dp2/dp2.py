from abc import ABC, abstractmethod
from enum import Enum


class Pizza(ABC):

    def __init__(self, crust_type, size, *toppings):
        self._crust = crust_type
        self._size = size
        self._toppings = toppings

    @abstractmethod
    def bake(self):
        raise NotImplemented()

    def __str__(self):
        return f"{self.__class__.__name__}: {self._toppings}"


class PepperoniPizza(Pizza):
    def bake(self):
        print("Baking pepperoni")

class CheesePizza(Pizza):
    def bake(self):
        print("Baking cheese pizza")

class MeatLoversPizza(Pizza):
    def bake(self):
        print("Baking meat lovers pizza")


class VeggiePizza(Pizza):
    def bake(self):
        print("Baking veggie pizza")



class PizzaFactory:
    class MEAT_TOPPINGS(Enum):
        PEPPERONI = 'pepperoni'
        SALAMI = 'salami'
        CHICKEN = 'chicken'
        SAUSAGE = 'sausage'

    class CHEESE_TOPPINGS(Enum):
        PARMESAN = 'parmesan'
        CHEDDAR = 'cheddar'
        MOZZARELLA = 'mozzarella'
        GOUDA = 'gouda'


    @staticmethod
    def getPizza(*toppings, crust_type='standard', size='family'):

        cheese_toppings_num = len(set(e.value for e in PizzaFactory.CHEESE_TOPPINGS)
                                  .intersection(set(toppings)))
        meat_toppings_num = len(set(e.value for e in PizzaFactory.MEAT_TOPPINGS)
                                .intersection(set(toppings)))

        toppings = [t.lower() for t in toppings]
        if meat_toppings_num > 3:
            return MeatLoversPizza(crust_type, size, *toppings)
        elif PizzaFactory.MEAT_TOPPINGS.PEPPERONI in toppings:
            return PepperoniPizza(crust_type, size, *toppings)
        elif cheese_toppings_num > 2:
            return CheesePizza(crust_type, size, *toppings)
        elif cheese_toppings_num == 0 and meat_toppings_num == 0:
            return VeggiePizza(crust_type, size, *toppings)
        else:
            raise Exception()


if __name__ == '__main__':
    p1 = PizzaFactory.getPizza('corn', 'gouda', 'parmesan', 'cheddar')
    print(p1)
    p1.bake()

    p2 = PizzaFactory.getPizza('tomato', 'corn')
    print(p2)
    p2.bake()
