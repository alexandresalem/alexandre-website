from django.test import TestCase

from gamef1.models import F1Prediction


class F1TestCase(TestCase):
    def setUp(self):
        self.count = 19

    def test_f1_car_exists(self):
        
        self.assertGreater(self.count, 12)
