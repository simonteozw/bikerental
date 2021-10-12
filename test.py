import unittest
from datetime import datetime, timedelta
from bikerental import BikeRental
from customer import Customer

class BikeRentalTest(unittest.TestCase):
    def test_BikeRental_display_correct_stock(self):
        shop1 = BikeRental()
        shop2 = BikeRental(10)
        self.assertEqual(shop1.displaystock(), 0)
        self.assertEqual(shop2.displaystock(), 10)

    def test_rentNegativeBikes(self):
        shop1 = BikeRental()
        self.assertEqual(shop1.rentBikeHour(-10), None)

    def test_rent0Bikes(self):
        shop1 = BikeRental()
        self.assertEqual(shop1.rentBikeHour(0), None)

    def test_rentTooManyBikes(self):
        shop1 = BikeRental(5)
        self.assertEqual(shop1.rentBikeHour(6), None)

    def test_rentValidBikes(self):
        shop1 = BikeRental(5)
        hour = datetime.now().hour
        self.assertEqual(shop1.rentBikeHour(3).hour, hour)

    def test_returnBike_invalidNum(self):
        shop = BikeRental(10)

        customer = Customer()
        customer.rentalTime = datetime.now()
        customer.bikes = 0
        request = customer.returnBike()

        self.assertIsNone(shop.returnBike(request))

class CustomerTest(unittest.TestCase):
    def test_returnBike_validInput(self):
        customer = Customer()
        now = datetime.now()
        customer.rentalTime = now
        customer.bikes = 4
        self.assertEqual(customer.returnBike(),(now, 4))

    def test_returnBike_InvalidInput(self):
        customer = Customer()
        now = datetime.now()
        customer.rentalTime = now
        customer.bikes = None
        self.assertEqual(customer.returnBike(),(None, None))

if __name__ == "__main__":
    unittest.main()