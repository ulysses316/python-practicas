#AIzaSyAkvnibhwMbVxZCQFLinExVyYbV8pE0aJI
import requests
class Ubicacion:
    def peticion(self,latlng):
        a=requests.get(params={"latlng":latlng,"key":"AIzaSyAkvnibhwMbVxZCQFLinExVyYbV8pE0aJI"},url="https://maps.googleapis.com/maps/api/geocode/json").json()
        numero=a["results"][0]["address_components"][0]["long_name"]
        calle=a["results"][0]["address_components"][1]["long_name"]
        print numero
        print calle

peticion(19.598531,-99.053072)
