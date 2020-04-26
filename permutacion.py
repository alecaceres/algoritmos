class nodo:
    def __init__(self, n, valor = "", permutacion = ""):
        self.valor = valor
        self.tamano = n
        self.permutacion = str(valor) + permutacion
        if n:
            self.hijos = [nodo(n-1, 0, self.permutacion), nodo(n-1, 1, self.permutacion)]
        else:
            self.hijos = []
            self.permutacion = self.permutacion + "\n"

def dfs(a):
    if a.tamano:
        for hijo in a.hijos:
            dfs(hijo)
    else:
        print(a.permutacion, end = "")

a = input('Ingrese la cantidad de bits: ')
dfs(nodo(int(a)))
