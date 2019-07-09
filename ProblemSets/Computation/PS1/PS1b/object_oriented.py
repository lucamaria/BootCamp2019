class Backpack:
    """A Backpack object class. Has a name and a list of contents.
    Attributes:
    name (str): the name of the backpack's owner.
    contents (list): the contents of the backpack.
    """

    def __init__(self, name, color, max_size=5):
        """Set the name and initialize an empty list of contents.
        Parameters:
        name (str): the name of the backpack's owner.
        color (str): color of the backpack
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the backpack.
        """
        self.name=name
        self.color=color
        self.max_size=5
        self.contents = []

    def put(self, item):
        """Add 'item' to the backpack's list of contents."""
        if len(self.contents)<= self.max_size:
            self.contents.append(item)
        if len(self.contents)> self.max_size:
            print("No Room!")
            self.contents.remove(item)
            """Remove 'item' from backpack's list as there is no more space."""

    def take(self, item):
        """Remove 'item' from the backpack's list of contents."""
        self.contents.remove(item)

    def dump(self):
        """Remove 'item' from the backpack's list of contents."""
        self.contents=list()

    def __add__(self, other):
        """Add the number of contents of each Backpack."""
        return len(self.contents) + len(other.contents)

    def __lt__(self, other):
        """If 'self' has fewer contents than 'other', return True.
        Otherwise, return False.
        """
        return len(self.contents) < len(other.contents)

    def __eq__(self, other):
        """If 'self' has the same name, color and number of contents than, return True.
        Otherwise, return False.
        """
        return self.name==other.name and self.color==other.color and len(self.contents) == len(other.contents)

    def __str__(self):
        return "Owner: "+self.name+" "+"Color: "+self.color+" "+"Size: "+str(len(self.contents))+" "+"Max Size: "+str(self.max_size)+" "+"Contents: "+str(self.contents)

class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.
    Attributes:
    name (str): the name of the knapsack's owner.
    color (str): the color of the knapsack.
    max_size (int): the maximum number of items that can fit inside.
    contents (list): the contents of the backpack.
    closed (bool): whether or not the knapsack is tied shut.
    """

    def __init__(self, name, color, max_size=3):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A knapsack only holds 3 item by default.
        Parameters:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        """
        Backpack.__init__(self, name, color, max_size)
        self.closed = True

    def put(self, item):
        """If the knapsack is untied, use the Backpack.put() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.put(self, item)

    def take(self, item):
        """If the knapsack is untied, use the Backpack.take() method."""
        if self.closed:
            print("I'm closed!")

        else:
            Backpack.take(self, item)

    def weight(self):
        return sum([len(str(item)) for item in self.contents])

class Jetpack(Backpack):
    """A Jetpack object class. Inherits from the Backpack class.
    Calculate the weight of the knapsack by counting the length of the
    string representations of each item in the contents list.
    name (str): the name of the knapsack's owner.
    color (str): the color of the knapsack.
    max_size (int): the maximum number of items that can fit inside.
    contents (list): the contents of the backpack.
    fuel (int): amount of fuel available to be burnt.
    """

    def __init__(self, name, color, max_size=2, fuel = 10):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A knapsack only holds 4 item by default.
        Parameters:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        fuel (int): amount of fuel available to be burnt.
        """
        Backpack.__init__(self, name, color, max_size)
        self.fuel = 10

    def fly(self):
        """Fuel is burnt when flying until the tank is empty."""
        if self.fuel > 0:
            self.fuel = self.fuel-1
            return self.fuel
        if self.fuel ==0:
            print("Not enough fuel!")
    def dump(self):
        """Remove 'item' from the list of contents and all fuel
        from the tank"""
        self.contents=list()
        self.fuel=list()
