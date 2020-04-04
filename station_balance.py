from statistics import mean
def imbalance(C, S, masses):
    masses.sort()
    A = sum(masses)/C
    padding = [0]*(2*C-S)
    masses = padding + masses
    imbalance = 0
    for i in range(C):
        print("Contenedor", i, "\t", masses[i], masses[2*C-i-1])
        Xi = (masses[i] + masses[2*C-i-1])
        imbalance += abs(Xi-A)
    print("Imbalace=", imbalance, '\n')


C = 2
S = 3
masses = [6, 3, 8]
imbalance(C, S, masses)
