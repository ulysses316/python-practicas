import random


def juego():
  print "Hola vamos a jugar piedra papel o tijeras:"
  print "0.........piedra"
  print "1.........papel"
  print "2.........tijeras"
  opcion=int(raw_input("Elige una opcion: "))
  if opcion == 0:
    maquina=random.randrange(2)
    print "Maquina eligio %i"% maquina
    if maquina==1:
      print "La maquina gana"
    if maquina==0:
      print "Es un empate"
    if maquina==2:
      print "El jugador gana"

  if opcion == 1:
    maquina=random.randrange(2)
    print "Maquina eligio %i"% maquina
    if maquina==2:
      print "La maquina gana"
    if maquina==1:
      print "Es un empate"
    if maquina==0:
      print "El jugador gana"

  if opcion == 2:
    maquina=random.randrange(2)
    print "Maquina eligio %i"% maquina
    if maquina==0:
      print "La maquina gana"
    if maquina==2:
      print "Es un empate"
    if maquina==1:
      print "El jugador gana"


juego()
