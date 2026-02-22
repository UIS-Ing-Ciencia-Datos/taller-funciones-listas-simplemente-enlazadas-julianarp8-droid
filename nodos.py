# Clase Nodo
class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None


# Clase Lista Enlazada Simple
class ListaSE:
    def __init__(self):
        self.cabeza = None

    # Insertar al final
    def insertarFinal(self, data):
        nuevo = Nodo(data)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo

    # Insertar después de un valor X
    def insertarDespues(self, valorX, nuevoValor):
        actual = self.cabeza

        while actual:
            if actual.data == valorX:
                nuevo = Nodo(nuevoValor)
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
                return
            actual = actual.siguiente

        print("Elemento no encontrado")

    # Insertar antes de un valor X
    def insertarAntes(self, valorX, nuevoValor):
        if self.cabeza is None:
            print("Lista vacía")
            return

        # Si es el primero
        if self.cabeza.data == valorX:
            nuevo = Nodo(nuevoValor)
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return

        actual = self.cabeza

        while actual.siguiente:
            if actual.siguiente.data == valorX:
                nuevo = Nodo(nuevoValor)
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
                return
            actual = actual.siguiente

        print("Elemento no encontrado")

    # Eliminar el primero
    def eliminarPrimero(self):
        if self.cabeza is None:
            print("Lista vacía")
            return

        self.cabeza = self.cabeza.siguiente

    # Eliminar el último
    def eliminarUltimo(self):
        if self.cabeza is None:
            print("Lista vacía")
            return

        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

        actual = self.cabeza
        while actual.siguiente.siguiente:
            actual = actual.siguiente

        actual.siguiente = None

    # Buscar elemento (True o False)
    def buscar(self, valor):
        actual = self.cabeza

        while actual:
            if actual.data == valor:
                return True
            actual = actual.siguiente

        return False

    # Contar elementos
    def contar(self):
        contador = 0
        actual = self.cabeza

        while actual:
            contador += 1
            actual = actual.siguiente

        return contador

    # Imprimir lista
    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.data, end=" -> ")
            actual = actual.siguiente
        print("None")

        
