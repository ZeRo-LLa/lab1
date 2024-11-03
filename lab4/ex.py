class TouristVoucher:
    def __init__(self, country="", duration=0, price=0.0, rating=0, description=""):
        print("Object created:")
        self.set_country(country)
        self.set_duration(duration)
        self.set_price(price)
        self.rating = rating
        self.description = description


    def get_country(self):
        return self.__country
    def get_duration(self):
        return self.__duration
    def get_price(self):
        return self.__price
    
    def set_duration(self, duration):
        self.__duration = duration
    def set_price(self, price):
        self.__price = price
    def set_country(self, country):
        self.__country = country


    def __str__(self):
        return (f"Tourist Voucher: Country={self.__country}, "
                f"Duration={self.__duration} days, Price={self.__price}€, "
                f"Rating={self.rating}, Description='{self.description}'")

    def __repr__(self):
            print("Calling repr")
            return self.__str__()

    def __del__(self):
        print(f"Deleting Tourist Voucher for {self.__country}")

def main():
    voucher1 = TouristVoucher("France", 7, 1200, 5, "Romantic trip to Paris")
    voucher2 = TouristVoucher("Japan", 14, 2500, 4, "Cultural exploration")
    voucher3 = TouristVoucher("Italy", 10, 1500, 5, "Gourmet food tour")

    print(voucher1)
    print(voucher2)
    print(voucher3)

main()
