
import unittest
import calc

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        # اختبار دالة الجمع: هل 2 + 3 يساوي 5؟
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)

    def test_subtract(self):
        # اختبار دالة الطرح: هل 5 - 2 يساوي 3؟
        self.assertEqual(calc.subtract(5, 2), 3)
        self.assertEqual(calc.subtract(2, 2), 0)

if name == 'main':
    unittest.main()
