from enum import Enum

class Taste(Enum):
    SWEET = "Sweet"
    SOUR = "Sour"
    NEUTRAL = "Neutral"

class Fruit:
    def __init__(self, name, size, color, taste):
        self.__name = name
        self.__size = size
        self.__color = color
        self.__taste = taste
    #getters
    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color

    def get_taste(self):
        return self.__taste
    #setters
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
    #repr method
    def __repr__(self):
        return f"Fruit(name='{self.__name}', size={self.__size}, color='{self.__color}', taste={self.__taste})"
    #destructor
    def __del__(self):
        print(f"{self.__name} deleted")

#Topping for salad
class Topping(Enum):
    WHIPPED_CREAM = ("Whipped Cream", Taste.SWEET)
    CHOCOLATE_SYRUP = ("Chocolate Syrup", Taste.SWEET)
    HONEY = ("Honey", Taste.SWEET)
    YOGURT = ("Yogurt", Taste.NEUTRAL)
    LEMON_JUICE = ("Lemon Juice", Taste.SOUR)

    def __init__(self, description, taste):
        self.description = description
        self.taste = taste

#fruit salad
class FruitSalad:
    def __init__(self, fruits, topping):
        self.__fruits = fruits 
        self.__topping = topping

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
        self.__fruits.append(fruit)

    #Function for choosing topping
    def choose_topping_based_on_taste(self):
        sweet_count = 0
        sour_count = 0

        for fruit in self.__fruits:
            if fruit.get_taste() == Taste.SWEET:
                sweet_count += 1
            elif fruit.get_taste() == Taste.SOUR:
                sour_count += 1

        if sweet_count > sour_count:
            self.__topping = Topping.HONEY
        elif sour_count > sweet_count:
            self.__topping = Topping.LEMON_JUICE
        else:
            self.__topping = Topping.YOGURT

    def __repr__(self):
        fruit_list = ", ".join(repr(fruit) for fruit in self.__fruits)
        return f"FruitSalad(fruits=[{fruit_list}], topping={self.__topping.description})"

    def __del__(self):
        print("FruitSalad deleted")

def main():
    apple = Fruit("Apple", 150, "Red", Taste.SWEET)
    lemon = Fruit("Lemon", 100, "Yellow", Taste.SOUR)
    banana = Fruit("Banana", 120, "Yellow", Taste.SWEET)

    salad = FruitSalad([apple, lemon, banana], Topping.WHIPPED_CREAM)
    print(salad)

    salad.choose_topping_based_on_taste()
    print("After choosing topping based on taste:")
    print(salad)

main()
