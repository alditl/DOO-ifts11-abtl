#Una "Coleccion" contiene varios documentos 
#Represento con diccionarios

from documento import Documento
from str2doc import str2Doc
class Coleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}  

    def anadir_documentos(self, documento):
        self.documentos[documento.id] = documento

    def eliminar_documento(self, id_documento):
        if id_documento in self.documentos:
            del self.documentos[id_documento]

    def buscar_documento(self, id_documento):
        return self.documentos.get(id_documento, None)
    
    def importardoc(self, rutacsv):
        with open(rutacsv, 'r') as file:
            contenido = file.readline().replace('\n', '') #Reemplazar el \n(saltodelinea) por caracter vacío 
            str2 = str2Doc(contenido)
            linea = file.readline()
            auto = 0
            while linea != "":
                nuevo_doc = Documento(auto, str2.convert(linea.strip('\n')))
                self.anadir_documentos(nuevo_doc)
                auto = auto + 1
                linea = file.readline()
    # C:\\Users\\aldut\\Desktop\\IFTS11\\DESARROLLO DE SIS O.O\\DOO-ifts11-abtl\\files\\BBDD.csv                



    def listar_documento(self) -> list[Documento]:
        total = []
        for i in self.documentos:
            total.append(self.documentos[i])
        return total

    def __str__(self):
        return f"Coleccion {self.nombre} con len{(self.documentos)} "