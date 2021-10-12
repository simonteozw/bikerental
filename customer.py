import datetime

class Customer():
    def __init__(self):
        self.bikes = 0
        self.bill = 0
        self.rentalTime = 0

    def requestBike(self):
        bikes = input("How many bikes would you like to rent?")

        try:
            bikes = int(bikes)
        except ValueError:
            print("Bikes should be a positive inter greater than 0.")
            return None

        if bikes < 1:
            print("Bikes should be a positive inter greater than 0.")
            return None

        self.rentalTime = datetime.datetime.now()
        self.bikes = bikes
        return bikes

    def returnBike(self):
        if self.rentalTime and self.bikes:
            return self.rentalTime, self.bikes

        return None, None
