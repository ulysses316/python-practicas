import requests

#class Geocodificacion:

def peticion():
    origen=raw_input("Dame la direccion de origen: ")
    a=requests.get(params={"address":origen,"key":"AIzaSyA-A9tiTGkosbXccQ9uaGDDKCOhKzOK6jU"}, url="https://maps.googleapis.com/maps/api/geocode/json").json()
    lat=a["results"][0]["geometry"]["location"]["lat"]
    lng=a["results"][0]["geometry"]["location"]["lng"]


def peticion_destino():
    destino=raw_input("Dame la direccion del destino :")
    a=requests.get(params={"address":destino,"key":"AIzaSyA-A9tiTGkosbXccQ9uaGDDKCOhKzOK6jU"}, url="https://maps.googleapis.com/maps/api/geocode/json").json()
    lat1=a["results"][0]["geometry"]["location"]["lat"]
    lng1=a["results"][0]["geometry"]["location"]["lng"]

def distance():
    a=requests.get(params={"origins":"19.483762, -99.246336","destinations":"19.603224, -99.056224","key":"AIzaSyAAsTwpyJWBDtzLL4_YDI6YDu1OJADhyI0"},url="https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial").json()
    print a
