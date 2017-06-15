import random
almacen=[]
almacen.append("sala troncoso")
almacen.append("maravilloso teatro en casa sony")
almacen.append("boleto de metro")
print (almacen)
catafixia=[]
catafixia.append([])
catafixia.append([])
catafixia.append([])
catafixia[0].append("sala troncoso")
catafixia[1].append("maravilloso teatro en casa sony")
catafixia[2].append("boleto de metro")
print (catafixia[2])
print(random.randrange(3))
if random.randrange(3) == 0:
    print("Te ganaste una sala troncoso!!!")
if random.randrange(3) == 1:
    print("Te ganaste un maravilloso teatro en casa en sony")
if random.randrange(3) == 2:
    print("Te ganaste un maravilloso boleto de metro")
