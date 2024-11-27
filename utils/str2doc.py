
class str2Doc (object):
    def __init__ (self, schema, separator=","):
        self.separator = separator
        self.keys = schema.split(separator)
    def convert(self, line):
        values = line.split(self.separator)
        if len(values) == len(self.keys):
            diccionario = {}
            i = 0
            while i < len(self.keys):
                diccionario[self.keys[i]] = values[i]
                i = i + 1
            return diccionario


s2d = str2Doc("Nombre,Apellido,Edad,Email,Telefono")
print(s2d.keys)
print(s2d.convert("Juan,García,27,juan.garcía@ejemplo.com,555-0122-5544"))


