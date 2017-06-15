import requests
w=raw_input("Dame punto de origen ")
r = requests.get(params={"make":"SD","type":"json","buscar":w,"key":"IS9ANsMy-yppD-85yo-YqnF-ysgVdOaSpDZc"},url='http://gaia.inegi.org.mx/sakbe/wservice').json()
dest_i=r[0]["id_dest"]

w=raw_input("Dame destino ")
r = requests.get(params={"make":"SD","type":"json","buscar":w,"key":"IS9ANsMy-yppD-85yo-YqnF-ysgVdOaSpDZc"},url='http://gaia.inegi.org.mx/sakbe/wservice').json()
dest_f=r[0]["id_dest"]

#CR
r1 = requests.get(params={"make":"CR","type":"json","v":1,"dest_i":dest_i,"dest_f":dest_f,"key":"IS9ANsMy-yppD-85yo-YqnF-ysgVdOaSpDZc"},url='http://gaia.inegi.org.mx/sakbe/wservice').json()
costo=r1[0]["costo_caseta"]
print ("${} es lo que se gastara en casetas").format(costo)

r = requests.get('http://gaia.inegi.org.mx/sakbe/wservice?make=CM&type=json&key=IS9ANsMy-yppD-85yo-YqnF-ysgVdOaSpDZc').json()
magna=r[0]["costo"]
premium=r[1]["costo"]
diesel=r[2]["costo"]
gas=r[3]["costo"]
