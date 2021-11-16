import unittest
from ejemplo import *

class TestEjemplo(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(15, 5), 20)

    def test_restar(self):
        self.assertEqual(restar(20, 5), 15)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 5), 25)

    def test_dividir(self):
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividirSinResto(self):
        self.assertEqual(dividirSinResto(5, 2), 2)

if __name__ == "__main__":
    unittest.main()