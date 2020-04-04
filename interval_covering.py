import sys

def intervals(X):
    print("X =", X)
    X.sort()
    print("\nX ordenado:", X)
    S = recursion(X, [])
    print("\nS=", S, "\n\n\n")


def recursion(X,S):
    if X:
        S.append((X[0], X[0]+1))
        X = list(filter((X[0]+1).__le__, X))
        return recursion(X, S)
    return S

for i, line in enumerate(sys.stdin):
    print("------------------------------------\nTest", i+1, end = "\n\n")
    linea = line.rstrip()
    X = [float(x) for x in linea.split()]
    intervals(X)
