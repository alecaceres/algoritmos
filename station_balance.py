from statistics import mean
import sys

def imbalance(C, S, masses):
    sorted = masses.copy()
    sorted.sort()
    A = sum(masses)/C

    padding = [0]*(2*C-S)
    sorted = padding + sorted
    imbalance = 0
    counter = 0
    for i in range(len(masses)):
        if masses[i] in sorted:
            print(" "+str(counter)+":", masses[i], end = '')
            index_0 = sorted.index(masses[i])
            index_1 = len(sorted) - index_0 - 1
            if sorted[index_1]: print("", sorted[index_1])
            else: print()
            Xi = (sorted[index_0] + sorted[index_1])
            imbalance += abs(Xi-A)
            if index_1<index_0: index_0, index_1 = index_1, index_0
            del sorted[index_1]
            del sorted[index_0]
            counter+=1
    for i in range(counter, C):
        print(" "+str(i)+":")
        imbalance += abs(A)
    print("IMBALANCE = {:.5f}".format(round(imbalance, 5)) + '\n')

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
