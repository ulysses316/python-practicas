class Animal(object):
  num_animal=0
  def __init__(self,nombre,raza):
    self.nombre=nombre
    self.raza=raza
    Animal.num_animal+=1
  def hablar(self):
    print"El {} {} dice Hola".format(self.raza,self.nombre)

class Perro(Animal):
  num_perros=0
  def __init__(self,nombre,raza):
    Animal.__init__(self,nombre,raza)
    Perro.num_perros+=1
  def aullar(self):
    print "El {} {} dice WOOF".format(self.raza,self.nombre)

class Gato(Animal):
  num_gato=0
  def __init__(self,nombre,raza):
    Animal.__init__(self,nombre,raza)
    Gato.num_gato+=1
  def maullar(self):
    print "El {} {} dice MEOW".format(self.raza,self.nombre)


dingo=Perro("Dingo","Chihuahua")
alushe=Perro("Alushe","Puddle")
manchita=Perro("Manchita","Boxer")

ringo=Gato("Ringo","Chih")
estuche=Gato("Estuche","Pud")
scrable=Gato("Escrable","Box")

alushe.aullar
