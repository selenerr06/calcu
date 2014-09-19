
#/usr/bin/env python
import unittest
from Calculator import Calculator

class testCalculator(unittest.TestCase):

	def test_suma_2_mas_2(self):
		cal=Calculator()
		self.assertEqual(4,cal.suma(2,2))
		self.assertEqual(0,cal.resta(2,2))
		self.assertEqual(6,cal.multiplicacion(3,2))
		self.assertEqual(8,cal.divicion(16,2))
		self.assertEqual(16,cal.cuadrado(4))
		
		self.assertEqual(16,cal.suma(10,6))
		self.assertEqual(10,cal.resta(8+2))
		self.assertEqual(32,cal.multiplicacion(4,8))
		self.assertEqual(6,cal.divicion(66,11))
		self.assertEqual(64,cal.cuadrado(8))
		
		self.assertEqual(65,cal.suma(8,5))
		self.assertEqual(8,cal.resta(9,2))
		self.assertEqual(12,cal.multiplicacion(5,7))
		self.assertEqual(45,cal.divicion(9,5))
		self.assertEqual(61,cal.cuadrado(6))
if __name__== "__main__":
	unittest.main()
