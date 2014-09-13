
# -*- coding: utf8 -*-
"""
>>> anotar('1')
'anoto jugador 1  con 15'

>>> anotar('1')
'anoto jugador 1  con 15'

>>> anotar('1')
'anoto jugador 1  con 10'

>>> anotar('1')
'anoto jugador 1  con 15'

>>> mostrarScore()
'jugador1: setGanados:1 puntuje:15 jugador2 setGanados:1 puntuje:0'

>>> mostrarScore()
'jugador1: setGanados:1 puntuje:15 jugador2 setGanados:0 puntuje:0'

>>> anotar('2')
'anoto jugador 2  con 10'

>>> anotar('2')
'anoto jugador 2  con 15'

>>> mostrarScore()
'jugador1: setGanados:1 puntuje:0 jugador2 setGanados:0 puntuje:15'

>>> anotar('2')
'anoto jugador 2  con 15'


>>> anotar('1')
'anoto jugador 1  con 15'

>>> mostrarScore()
'jugador1: setGanados:1 puntuje:15 jugador2 setGanados:0 puntuje:40'

"""
def anotar(noJugador):
	tipo=''
	global jugador1
	global jugador2
	global setsGanado1
	global setsGanado2
	global ganado1
	global ganado2
	
	if noJugador=='1':
		if jugador1==0:
			jugador1+=15
			tipo='15'
		elif jugador1==15:
			jugador1+= 15
			tipo='15'
		elif jugador1==30:
			jugador1+=10
			tipo='10'
		elif jugador1==40:
			jugador1= 0
			setsGanado1+=1
			tipo='set'
			if setsGanado1-2==setsGanado2:
				tipo='GANADO 1'
	elif noJugador=='2':
		if jugador2==0:
			jugador2+=15
			tipo='15'
		elif jugador2==15:
			jugador2+=15
			tipo='15'
		elif jugador2==30:
			jugador2+=10
			tipo='10'
		elif jugador2==40:
			jugador2=0
			setsGanado2+=+1
			tipo='set'
			if setsGanado2-2==setsGanado1:
				tipo='GANADO 2'
			
	if jugador1==40 or  jugador2==40:
		tipo=tipo+' deuce'
	
	return 'anoto jugador '+noJugador+'  con '+ tipo
		
def mostrarScore():
	return  'jugador1: setGanados:'+str(setsGanado1)+' puntuje:'+str(jugador1)+' ' +'jugador2 setGanados:'+str(setsGanado2)+' puntuje:'+str(jugador2)
			
	
jugador1=0
jugador2=0
setsGanado1=0
setsGanado2=0
ganado1=0
ganado2=0
