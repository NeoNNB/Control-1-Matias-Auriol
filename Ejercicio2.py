
from mailbox import NoSuchMailboxError
import json
import requests


def georeference(n):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    consulta = json.loads(response.text)
    lista=[]
    n=(input("ingrese un numero:"))
    nombre=(consulta[int(n)]['name'])
    longitud=(consulta[int(n)]['address']['geo']['lng'])
    latitud=(consulta[int(n)]['address']['geo']['lat'])
   
    lista.append([nombre])
    lista.append([latitud])
    lista.append([longitud])
    return lista
    
n=0
print(georeference(n))