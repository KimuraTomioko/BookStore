from django.test import TestCase
from shop.utils import sum_price_count, CalculateMoney

class CalculateMoneyDefTestCase(TestCase):
    def test_sum_count_price_pass(self):
        result = sum_price_count(500, 2)
        self.assertEqual(result, 1000)
    
    def test_sum_price_2_pass(self):
        result = sum_price_count(500, 1)
        self.assertEqual(result, 500)
    
    def test_sum_count(self):
        result = sum_price_count(price=200, count=15, discount=5)
        self.assertEqual(result, 2850)

class CalculateMoneyClassTestCase(TestCase):
    def setUp(self):
        self.calculator = CalculateMoney()
    
    def test_sum_count_price_pass(self):
        result = self.calculator.sum_price_count(price=100, count=10)
        self.assertEqual(result, 1000)
    
    def test_sum_price_pass(self):
        list_prices = [200, 640, 720]
        result = self.calculator.sum_price(list_prices)
        self.assertEqual(result, 1560)
    
    def test_sum_price_with_discount(self):
        list_prices = [200, 640, 720]
        result = self.calculator.sum_price(list_prices, discount=10)
        self.assertEqual(result, 1404)
    
    def test_sum_price_more_element(self):
        list_prices = [200, 640, 720, 100, 40]
        result = self.calculator.sum_price(list_prices)
        self.assertEqual(result, 1700)
