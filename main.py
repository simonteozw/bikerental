import datetime

class BikeRental():
    def __init__(self, stock=0):
        self.stock = 0

    def displaystock(self):
        print("We have currently {} bikes available to rent.".format(self.stock))
        return self.stock

