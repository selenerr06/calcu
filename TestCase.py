
#/usr/bin/env python
import unittest
from Figura import Figura

class TestCase():

	def test_es_rectangulo(self):
		fig=Figura()
		self.assertEqual("RECTANGULO",fig.figura("RECTANGULO"))
		
	def test_es_rectanguloaAREA(self):
		fig=Figura()
		self.assertEqual(12,fig.rectangulo(2,6))
	
	def test_es_rectanguloaAREA_2(self):
		fig=Figura()
		self.assertEqual(12,fig.rectangulo(3*4))

	################################################	
	def test_es_circulo(self):
		fig=Figura()
		self.assertEqual("CIRCULO",fig.figura("CIRCULO"))
	
	def test_es_circuloAREA(self):
		fig=Figura()
		self.assertEqual(113.0976,fig.circulo(6))
	
	def test_es_circuloAREA_2(self):
		fig=Figura()
		self.assertEqual(12.5664,fig.circulo(2))
	
	########################3
	def test_es_cuadrado(self):
		fig=Figura()
		self.assertEqual("CUADRADO",fig.figura("CUADRADO"))
		
	
	def test_es_cuadradoAREA(self):
		fig=Figura()
		self.assertEqual(4,fig.figura(2))
	
	def test_es_cuadradoAREA_2(self):
		fig=Figura()
		self.assertEqual(16,fig.cuadrado(4))
	
	####################3
	def test_es_tringulo(self):
		fig=Figura()
		self.assertEqual("TRIANGULO",fig.figura("TRIANGULO"))
	
	def test_es_tringuloAREA(self):
		fig=Figura()
		self.assertEqual(3,fig.tringulo(3,2))
	
	def test_es_tringuloAREA_2(self):
		fig=Figura()
		self.assertEqual(90,fig.tringulo(9,10))
		
	####################################	
	def test_es_rombo(self):
		fig=Figura()
		self.assertEqual("ROMBO",fig.figura("ROMBO"))
	
	def test_es_romboAREA(self):
		fig=Figura()
		self.assertEqual(17.5,fig.rombo(7,5))
	
	def test_es_romboAREA_2(self):
		fig=Figura()
		self.assertEqual(12.5,fig.rombo(6,5))	
	
	
		
		
	
if __name__== "__main__":
	unittest.main()
