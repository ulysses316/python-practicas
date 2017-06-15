import requests

def distancia():
    o=raw_input("Dame el punto de origen: ")
    d=raw_input("Dame el destino deseado: ")
    a=requests.get(params={"origins": o, "destinations":d}, url="https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&key=AIzaSyBfI7bob5KZFrPC4kQ-tzZzE63airiYsqU").json()
    print "La distancia entre los destinos es: ",a["rows"][0]["elements"][0]["distance"]["text"]
    print "El tiempo estimado de viaje es: ",a["rows"][0]["elements"][0]["duration"]["text"]
    w=a["rows"][0]["elements"][0]["distance"]["text"][0:3]
    km=float(w)
    cantidad_inicial=float(raw_input("Cuanta gasolina tenias al empezar el viaje: "))
    x=cantidad_inicial/km
    y=km/cantidad_inicial
    print "Gastas %.3f litros por kilometro "%(x)
    print "Recorres %.3f kilometros por litro"%(y)

distancia()
