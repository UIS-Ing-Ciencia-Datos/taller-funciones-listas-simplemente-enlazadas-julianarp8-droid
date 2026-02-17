class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
   
class ListaSimplementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def Vacio(self):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        else:
            print("La lista no está vacía.")
   
    def AgregarInicio(self, data):
        nuevoNodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
            return
        else:
            nuevoNodo.next = self.cabeza
            self.cabeza = nuevoNodo

    def AgregarFinal(self, data):
        nuevoNodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
            return
        else:
            actual = self.cabeza
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevoNodo
           
    def InsertarAntes(self, data):
        nuevoNodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
            return
        else:
            actual = self.cabeza
            while actual.next is not None:
                if actual.next.data == data:
                    nuevoNodo.next = actual.next
                    actual.next = nuevoNodo
                    return
                actual = actual.next
            print("El nodo con el valor especificado no se encontró.")
        