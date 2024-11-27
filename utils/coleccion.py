from documento import Documento

class Coleccion:
    def __init__(self, nombre):
        self.nombre: nombre
        self.documentos: {}  # type: ignore

    def anadir_documentos(self, documento):
        self.documentos[documento.id] = documento

    def eliminar_documento(self, id_documento):
        if id_documento in self.documentos:
            del self.documento[id_documento]

    def buscar_documento(self, id_documento):
        return self.documento.get(id_documento, None)

    def listar_documento(self) -> list[Documento]:
        total = []
        for i in self.documentos:
            total.append(self.documentos[i])
        return total

    def __str__(self):
        return f"Coleccion {self.nombre} con len{(self.documentos)} "