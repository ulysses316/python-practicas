calificaciones_grupoA= ['7', '5', '9', '7', '10', '6', '5', '9', '8', '8', '7', '8', '7', '8', '8', '9', '10', '5']
calificaciones_int=map(int,calificaciones_grupoA)
print(calificaciones_int)
filtro=filter(lambda x:x>8,calificaciones_int)
print filtro
filtro2=filter(lambda y:y>9,filtro)
print filtro2
