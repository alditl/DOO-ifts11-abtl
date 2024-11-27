import json

class Documento:
    def __init__(self, id, contenido=None):
        self.id = id
        self.contenido = contenido if contenido is not None else {}  #Otra forma de escribir un if: quiere decir que si contenido sea contenido si le paso parametro, si es None entonces que vaya vacio.
    
    def obtener_valor(self, clave):
        return self.contenido.get(clave, None)
    
    def modificar_valor(self, clave, valor):
        self.contenido[clave] = valor
    
    def __str__(self):
        return f"Documento(id={self.id}, contenido={self.contenido})"

# La clase `Documento` que representa un documento con un identificador único y un contenido basado en un diccionario.   

'''
__str__(): Es para los usuarios y se utiliza cuando quieres una representación fácil de leer del objeto. Se enfoca en la legibilidad.
__repr__(): Es para los desarrolladores y se utiliza cuando necesitas una representación más precisa o detallada, principalmente para depuración. Debe ser lo más detallada y precisa posible.
Si no se define __str__(), Python usará __repr__() como respaldo cuando se llame a
'''