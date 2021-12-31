import requests
from requests.models import Response

class opera:
    def lista(self):
        response = requests.get('http://localhost/web_trabajo/lista.php')
        return response.content #devuelve el contenido de la respuesta
    def agregar(self,id,sector,asiento,tarifa):
        response = requests.post('http://localhost/web_trabajo/agregar.php',data={'id':id,'sector':sector,'asiento':asiento,'tarifa':tarifa})
        return response.content #devuelve el contenido de la respuesta
    def filtro(self,sector):
        response = requests.get("http://localhost/web_trabajo/filtro.php?sector="+sector)
        return response.content #response.content es una variable que contiene el resultado de la funcion filtro    
    def sumar(self):
        response = requests.get("http://localhost/web_trabajo/suma.php")
        return response.content #response.content es una variable que contiene el resultado de la funcion sumar


