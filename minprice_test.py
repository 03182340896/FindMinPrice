import unittest
from minprice import FindMinPrice
class InputTests(unittest.TestCase):
    def test_input1(self):
        input_data = ('i1',)
        output = FindMinPrice('input.csv',input_data).get_best_price()
        self.assertEqual(output, ('1',1.0))

    def test_input2(self):
        input_data = ('i2',)
        output = FindMinPrice('input.csv',input_data).get_best_price()
        self.assertEqual(output, ('2',1.9))

    def test_input3(self):
        input_data = ('i2','i3')
        output = FindMinPrice('input.csv',input_data).get_best_price()
        self.assertEqual(output, ('1',4.0))

    def test_input4(self):
        input_data = ('i1','i4')
        output = FindMinPrice('input.csv',input_data).get_best_price()
        self.assertEqual(output, ('1',5.0))

    def test_input5(self):
        input_data = ('i2','i4')
        output = FindMinPrice('input.csv',input_data).get_best_price()
        self.assertEqual(output, ('2',5.9))

    def test_input6(self):
        input_data = ('i3','i4')
        output = FindMinPrice('input.csv',input_data).get_best_price()
        self.assertEqual(output, ('1',6.5))

    def test_input7(self):
        input_data = ('i2','i3','i4')
        output = FindMinPrice('input.csv',input_data).get_best_price()
        self.assertEqual(output, ('1',8))

    def test_input8(self):
        input_data = ('i1','i2','i3','i4')
        output = FindMinPrice('input.csv',input_data).get_best_price()
        self.assertEqual(output, ('2',8.45))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(InputTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
