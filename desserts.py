"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __init__(self, name, flavor, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0

        self.cache[self.name] = self 


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


    @classmethod
    def get(cls, name):
        """Return a cupcake from cache"""
        
        if name not in cls.cache:
            print("Sorry, that cupcake doesn't exist")
            return

        for cupcake in cls.cache:
            if cupcake == name:
                return cls.cache[cupcake]
        

    @staticmethod
    def scale_recipe(ingredients, amount):
        """Scale the list of ingredients by the given amount of cupcakes."""

        return [(ingredient, qty * amount) for ingredient, qty in ingredients]


    def add_stock(self, amount):
        """Add the amount of cupcakes in stock to qty attribute"""

        self.qty += amount

    
    def sell(self, amount):
        """Remove the amount sold from the qty available"""

        if self.qty == 0:
            print("Sorry, these cupcakes are sold out")
        elif self.qty - amount < 0:
            self.qty = 0
        else:
            self.qty -= amount

        

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
