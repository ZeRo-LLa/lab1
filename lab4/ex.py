class TouristVoucher:
    def __init__(self, country="", duration=0, price=0.0, rating=0, description="", hot_time = 0):
        print("Object created:")
        self.__country = country
        self.__duration = duration
        self.__price = price
        self.__hot_time = hot_time
        self.rating = rating
        self.description = description


    def get_country(self):
        return self.__country
    def get_duration(self):
        return self.__duration
    def get_price(self):
        return self.__price
    def get_hot_time(self):
        return self.__hot_time
    
    def set_duration(self, duration):
        self.__duration = duration
    def set_price(self, price):
        self.__price = price
    def set_country(self, country):
        self.__country = country
    def set_hot_time(self, hot_time):
        if hot_time >= 0:
            self.__hot_time -= hot_time
        return self.__hot_time

    def __str__(self):
        return (f"Tourist Voucher: Country={self.__country}, "
                f"Duration={self.__duration} days, Price={self.__price}€, "
                f"Rating={self.rating}, Description='{self.description}', Hot time={self.__hot_time}")

    def __repr__(self):
            print("Calling repr")
            return self.__str__()

    def __del__(self):
        print(f"Deleting Tourist Voucher for {self.__country}")
    

def main():
    voucher1 = TouristVoucher("France", 7, 1200, 5, "Romantic trip to Paris", 15)
    voucher2 = TouristVoucher("Japan", 14, 2500, 4, "Cultural exploration", 25)
    voucher3 = TouristVoucher("Italy", 10, 1500, 5, "Gourmet food tour", 30)

    print(voucher1)
    print(voucher2)
    print(voucher3)
    
    
    vouchers = [voucher1, voucher2, voucher3]
    for voucher in vouchers:
        voucher.set_hot_time(5)

    Min_voucher = vouchers[0]
    for voucher in vouchers:
        if voucher.get_hot_time() < Min_voucher.get_hot_time():
            Min_voucher = voucher

    print(f"The Hottest time is {Min_voucher.get_hot_time()}, {Min_voucher.get_country()}")
    
main()
