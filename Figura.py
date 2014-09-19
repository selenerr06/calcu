
#/usr/bin/env python
import unittest

class Figura():

	def figura(texto):
		self.regresa=""
		if(texto=="RECTANGULO"):
			self.regresa="RECTANGULO"
		if(texto=="CIRCULO"):
			self.regresa="CIRCULO"
		if(texto=="CUADRADO"):
			self.regresa="CUADRADO"
		if(texto=="TRIANGULO"):
			self.regresa="TRIANGULO"
		if(texto=="ROMBO"):
			self.regresa="ROMBO"
		return regresa;
	
	def circulo(radio):
		return 3.1415*radio*radio
	
	def rectangulo(lado1,lado2):
		return lado2*lado1
		
	def cuadrado(lado):
		return lado*lado
	
	def triangulo(base,altura):
		return (base*altura)/2
	
	def rombo(diagonal1, diagonal2):
		return (diagonal1*diagonal2)/2
