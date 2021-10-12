import datetime

class BikeRental():
    def __init__(self, stock=0):
        self.stock = stock

    def displaystock(self):
        print("We have currently {} bikes available to rent.".format(self.stock))
        return self.stock

    def rentBikeHour(self, n):
        if (n <= 0):
            print("Number of bikes must be positive.")
            return None

        if (n > self.stock):
            print("We can rent a maximum of {} bikes.".format(self.stock))
            return None

        now = datetime.datetime.now()
        print("You have rented {} bikes at hourly basis today at {} hours.".format(n, now.hour))
        self.stock -= n
        return now

    def returnBike(self, request):
        rentalTime, numBikes = request
        bill = 0

        if not (rentalTime and numBikes):
            print("Are you sure you rented a bike with us?")
            return None

        now = datetime.datetime.now()
        rentalPeriod = now - rentalTime

        bill = 5 * round(rentalPeriod.seconds/3600) * numBikes

        print("Thanks for returning your bike! The bill is {}.".format(bill))
        return bill

