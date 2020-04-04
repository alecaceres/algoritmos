def imbalance(C, S, masses):
    masses.sort()
    padding = [0]*(2*C-S)
    masses = padding + masses
    print(masses)



C = 2
S = 3
masses = [6, 3, 8]
imbalance(C, S, masses)
