from enum import Enum

# Enum for taste types
class Taste(Enum):
    SWEET = "Sweet"
    SOUR = "Sour"
    NEUTRAL = "Neutral"

# Fruit class
class Fruit:
    def __init__(self, name, size, color, taste):
        self.__name = name
        self.__size = size
        self.__color = color
        self.__taste = taste

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color

    def get_taste(self):
        return self.__taste

    def set_name(self, name):
        self.__name = name

    def set_size(self, size):
        self.__size = size

    def set_color(self, color):
        self.__color = color

    def set_taste(self, taste):
        if isinstance(taste, Taste):
            self.__taste = taste
        else:
            raise ValueError("Taste must be of type Taste Enum")

    def __repr__(self):
        """Returns a formal string representation of the fruit"""
        return f"Fruit(name='{self.__name}', size={self.__size}, color='{self.__color}', taste={self.__taste})"

    def __del__(self):
        """Destructor to delete a fruit object"""
        print(f"{self.__name} deleted")

class Topping(Enum):
    WHIPPED_CREAM = ("Whipped Cream", Taste.SWEET)
    CHOCOLATE_SYRUP = ("Chocolate Syrup", Taste.SWEET)
    HONEY = ("Honey", Taste.SWEET)
    YOGURT = ("Yogurt", Taste.NEUTRAL)
    LEMON_JUICE = ("Lemon Juice", Taste.SOUR)

    def __init__(self, description, taste):
        self.description = description
        self.taste = taste

class FruitSalad:
    def __init__(self, fruits, topping):
        self.__fruits = fruits    # Private field (list of fruits)
        self.__topping = topping  # Private field (topping)

    def get_fruits(self):
        return self.__fruits

    def get_topping(self):
        return self.__topping

    def set_fruits(self, fruits):
        if isinstance(fruits, list) and all(isinstance(fruit, Fruit) for fruit in fruits):
            self.__fruits = fruits
        else:
            raise ValueError("Fruits must be a list of Fruit objects")

    def set_topping(self, topping):
        if isinstance(topping, Topping):
            self.__topping = topping
        else:
            raise ValueError("Topping must be of type Topping Enum")

    def add_fruit(self, fruit):
        """Adds a fruit to the salad."""
        self.__fruits.append(fruit)

    def choose_topping_based_on_taste(self):
        """Chooses a topping based on the taste of the fruits."""
        sweet_count = sum(1 for fruit in self.__fruits if fruit.get_taste() == Taste.SWEET)
        sour_count = sum(1 for fruit in self.__fruits if fruit.get_taste() == Taste.SOUR)

        if sweet_count > sour_count:
            self.__topping = Topping.HONEY
        elif sour_count > sweet_count:
            self.__topping = Topping.LEMON_JUICE
        else:
            self.__topping = Topping.YOGURT

    def __repr__(self):
        """Returns a formal string representation of the fruit salad"""
        fruit_list = ", ".join(repr(fruit) for fruit in self.__fruits)
        return f"FruitSalad(fruits=[{fruit_list}], topping={self.__topping.description})"

    def __del__(self):
        """Destructor to delete a FruitSalad object"""
        print("FruitSalad deleted")

if __name__ == "__main__":
    apple = Fruit("Apple", 150, "Red", Taste.SWEET)
    lemon = Fruit("Lemon", 100, "Yellow", Taste.SOUR)
    banana = Fruit("Banana", 120, "Yellow", Taste.SWEET)

    salad = FruitSalad([apple, lemon, banana], Topping.WHIPPED_CREAM)
    print(salad)

    salad.choose_topping_based_on_taste()
    print("After choosing topping based on taste:")
    print(salad)
