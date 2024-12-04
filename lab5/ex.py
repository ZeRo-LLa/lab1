from enum import Enum

class Taste(Enum):
    SWEET = "Sweet"
    SOUR = "Sour"
    NEUTRAL = "Neutral"

class Topping(Enum):
    CHOCOLATE = ("Chocolate", Taste.SWEET)
    HONEY = ("Honey", Taste.SWEET)
    LEMON = ("Lemon", Taste.SOUR)
    CREAM = ("Cream", Taste.NEUTRAL)
    NUTS = ("Nuts", Taste.NEUTRAL)

    def __new__(cls, name, taste):
        obj = object.__new__(cls)
        obj._value_ = name
        obj.taste = taste
        return obj

class Fruit:
    def __init__(self, name, size, color, taste):
        self.name = name
        self.size = size
        self.color = color
        self.taste = taste

    def __str__(self):
        return f"{self.name} ({self.color}, {self.size}, {self.taste.value})"

class FruitSalad:
    def __init__(self, name, fruits=None, topping=None, cost_price=0, sell_price=0):
        self.name = name
        self.fruits = fruits if fruits else []
        self.topping = topping
        self.cost_price = cost_price
        self.sell_price = sell_price

    def add_fruit(self, fruit):
        self.fruits.append(fruit)

    def choose_topping(self):
        taste_count = {Taste.SWEET: 0, Taste.SOUR: 0, Taste.NEUTRAL: 0}
        for fruit in self.fruits:
            taste_count[fruit.taste] += 1
        dominant_taste = max(taste_count, key=taste_count.get)
        for topping in Topping:
            if topping.taste == dominant_taste:
                self.topping = topping
                break

    def shuffle_ingredients(self):
        import random
        random.shuffle(self.fruits)

    def set_prices(self):
        print(f"\n{self.name}")
        print("What it contains:")
        for fruit in self.fruits:
            print(f"- {fruit}")
        print(f"Topping: {self.topping.name if self.topping else 'None'}")
        while True:
            try:
                self.cost_price = float(input("Enter its cost price (e.g., 100): "))
                self.sell_price = float(input("Enter its selling price (e.g., 150): "))
                if self.cost_price <= 0 or self.sell_price <= 0:
                    print("Prices must be positive numbers. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter numeric values.")

    def profitability(self):
        return self.sell_price / self.cost_price if self.cost_price > 0 else 0

    def __str__(self):
        fruits_str = ", ".join([str(fruit) for fruit in self.fruits])
        return f"Fruits: [{fruits_str}], Topping: {self.topping.name if self.topping else 'None'}"

def main():
    apple = Fruit("Apple", "Medium", "Red", Taste.SWEET)
    lemon = Fruit("Lemon", "Small", "Yellow", Taste.SOUR)
    banana = Fruit("Banana", "Large", "Yellow", Taste.SWEET)
    kiwi = Fruit("Kiwi", "Small", "Green", Taste.SOUR)
    grape = Fruit("Grape", "Small", "Purple", Taste.NEUTRAL)

    salad1 = FruitSalad("Salad1", [apple, banana])
    salad2 = FruitSalad("Salad2", [lemon, kiwi])
    salad3 = FruitSalad("Salad3", [apple, grape, banana])
    salad4 = FruitSalad("Salad4", [grape, kiwi])
    salad5 = FruitSalad("Salad5", [lemon, apple])

    for salad in [salad1, salad2, salad3, salad4, salad5]:
        salad.choose_topping()
        salad.set_prices()

    salads = [salad1, salad2, salad3, salad4, salad5]
    n = len(salads)
    for i in range(n):
        for j in range(0, n - i - 1):
            if salads[j].profitability() < salads[j + 1].profitability():
                salads[j], salads[j + 1] = salads[j + 1], salads[j]

    print("\nTop 5 salads by profitability:")
    for index, salad in enumerate(salads[:5], start=1):
        profitability_percentage = (salad.profitability() - 1) * 100
        print(f"{index}. {salad.name}: {salad} -- Profitability: {profitability_percentage:.2f}%")

main()

