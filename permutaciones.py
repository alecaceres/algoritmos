class arbol:
    def __init__(self,n):
        if n:
            self.nodos = {nodo(0, n), nodo(1, n)}
        else:
            self.nodos = set()

    def __str__(self):
        for node in self.nodos:
            print("Hola", node)
        return ""

class nodo:
    def __init__(self, valor, n):
        self.valor = valor
        if n:
            self.hijos = {nodo(0, n-1), nodo(1, n-1)}
        else:
            self.hijos = set()

    def __str__(self):
        if self.hijos:
            for hijo in self.hijos:
                return str(hijo.valor)
        return "\n"

a = arbol(3)
print(a)
print("Nodos:", a.nodos)
for nodito in a.nodos:
    print("\nNodo:", nodito)
    for hijo in nodito.hijos:
        print("Hijo:", hijo)
        for hijito in hijo.hijos:
            print("Hijito:", hijito)
