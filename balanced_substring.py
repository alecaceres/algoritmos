import sys
import ctypes

def length(lista, mem, l, r):
    if mem[l][r]: return 0 # si esta posición ya fue visitada
    mem[l][r] = True # indica que esa posición ya fue visitada
    if not any(lista) or all(lista): return 0 # si todos los elementos son iguales
    if lista.count(0) == lista.count(1): return r-l+1 # está balanceada
    len_l = length(lista[0:-1], mem, l, r-1)
    len_r = length(lista[1:], mem, l+1, r)
    return max(len_l, len_r)

def reducir(lista, ratio, zeros, ones, N = 650, RATIO = 6):
    if ratio >= RATIO:
        if lista[0:N] == [0]*N:
            lista = lista[N:]
            if lista[0]: lista = lista[2:]
        if lista[-N:] == [0]*N:
            lista = lista[:-N]
            if lista[-1]: lista = lista[:-2]
    elif ratio <= 1/RATIO:
        if lista[0:N] == [1]*N:
            lista = lista[N:]
            if not lista[0]: lista = lista[2:]
        if lista[-N:] == [1]*N:
            lista = lista[:-N]
            if not lista[-1]: lista = lista[:-2]
    return lista.copy()

def respuesta(n, lista):
    if not any(lista) or all(lista): return 0
    c = 0
    N = len(lista)
    while (True):
        if len(lista)//35 == N: break
        N = len(lista)//35
        c += 1
        if not c%10: print(c, len(lista))
        if len(lista)<=120:
            break
        zeros = lista.count(0)
        ones = lista.count(1)
        if ones == 0 or zeros == 0: break
        ratio = zeros/ones
        lista = reducir(lista, ratio, zeros, ones, N = N)
    print("Reducido, len = ", len(lista), "iteraciones:", c)
    mem = (ctypes.c_bool * n * n)()
    return length(lista, mem, 0, len(lista)-1)

n, lista = [x for x in sys.stdin.readlines()]
lista = [int(x) for x in lista.rstrip()]
n = int(n)
print(respuesta(n, lista))
