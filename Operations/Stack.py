#Objeto de tipo Pila según el criterior Lifo
class Lifo_Queue:
    def __init__(self):
        self.objetos = []

    def __str__(self):
        return "{}".format(self.objetos)

    def push(self, elemento):
        self.objetos.append(elemento)

    def pop(self):
        try:
            return self.objetos.pop()
        except IndexError:
            raise ValueError("La lista no contiene elementos")
    
    def empty(self):
        return self.objetos == []

    def peek(self):
        return self.objetos[len(self.objetos) - 1]

