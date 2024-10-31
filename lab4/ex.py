class TouristVoucher:
    def __init__(self, country="", duration=0, price=0.0, rating=0, description=""):
        self.__country = country
        self.__duration = duration
        self.__price = price
        self.rating = rating
        self.description = description

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return (f"Tourist Voucher: Country={self.__country}, "
                f"Duration={self.__duration} days, Price={self.__price}€, "
                f"Rating={self.rating}, Description='{self.description}'")

    def __repr__(self):
        return (f"TouristVoucher(country='{self.__country}', "
                f"duration={self.__duration}, price={self.__price}, "
                f"rating={self.rating}, description='{self.description}')")

    def __del__(self):
        print(f"Deleting Tourist Voucher for {self.__country}")

def main():
    voucher1 = TouristVoucher("France", 7, 1200, 5, "Romantic trip to Paris")
    voucher2 = TouristVoucher("Japan", 14, 2500, 4, "Cultural exploration")
    voucher3 = TouristVoucher("Italy", 10, 1500, 5, "Gourmet food tour")

    print(voucher1)
    print(voucher2)
    print(voucher3)

if __name__ == "__main__":
    main()
