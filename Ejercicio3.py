import requests
import json

def comment(n):
    response= requests.get('https://jsonplaceholder.typicode.com/comments')
    consulta = json.loads(response.text)
    n=(input("ingrese un numero:"))
    library = {"comentario" : consulta[int(n)]['body']}
    return library

n=0
print(comment(n))