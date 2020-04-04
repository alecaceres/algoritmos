from statistics import mean
import sys

def imbalance(C, S, masses):
    masses.sort()
    A = sum(masses)/C
    padding = [0]*(2*C-S)
    masses = padding + masses
    imbalance = 0
    for i in range(C):
        print(str(i) + ":", end = '')
        if masses[i]: print("", masses[i], end = '')
        if masses[2*C-i-1]: print("", masses[2*C-i-1])
        Xi = (masses[i] + masses[2*C-i-1])
        imbalance += abs(Xi-A)
    print("Imbalace=", imbalance, '\n')

set_number = 1
for i, line in enumerate(sys.stdin):
    linea = line.rstrip() # se eliminan los saltos de línea de creados al leer las líneas de sys.stdin
    if i%2 == 0:
        C, S = [int(x) for x in linea.split()]
    else:
        masses = [int(x) for x in linea.split()]
        print("Set #"+str(set_number))
        imbalance(C, S, masses)
        set_number += 1
