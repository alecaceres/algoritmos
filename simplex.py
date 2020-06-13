def simplex(A, b, c):
    try: N, B, A, b, c, v = InitializeSimplex(A, b, c)
    except: return InitializeSimplex(A, b, c)
    while max(c) > 0:
        delta,  x_ = [[], []]
        e_index = c.index(max(c))
        e = sorted(list(N))[e_index]
        for i in sorted(list(B)):
            i_index = sorted(list(B)).index(i)
            if A[i_index][e_index] > 0: delta.append(b[i_index]/A[i_index][e_index])
            else: delta.append(float('inf'))
        l_index = delta.index(min(delta))
        if delta[l_index] == float('inf'): return "Unbounded"
        l = sorted(list(B))[l_index]
        N, B, A, b, c, v = pivot(N, B, A, b, c, v, l, e)
    for i in range(len(N)):
        if i in B:
            i_index = sorted(list(B)).index(i)
            x_.append(b[i_index])
        else: x_.append(0)
    return x_

def pivot(N, B, A, b, c, v, l, e):
    '''
    (N, B, A, b, c, v): programa lineal en la forma slack
    l: índice de la variable saliente
    e: índice de la variable entrante
    '''
    A_hat, b_hat, c_hat = [aux.copy() for aux in [A, b, c]]
    A_hat = [[None for i in range(len(N.union(B)))] for j in range(len(N.union(B)))]
    b_hat, c_hat = [[None for i in range(len(N.union(B)))] for j in range(2)]

    l_index = sorted(list(B)).index(l)
    e_index = sorted(list(N)).index(e)
    b_hat[e] = b[l_index]/A[l_index][e_index] # Computamos los nuevos coeficientes para la nueva variable básica xe
    for j in N.difference({e}):
        j_index = sorted(list(N)).index(j) #N.difference({e})?
        A_hat[e][j] = A[l_index][j_index]/A[l_index][e_index]
    A_hat[e][l] = 1/A[l_index][e_index]
    for i in sorted(list(B.difference({l}))): # Computamos los coeficientes de las dem ́as restricciones
        i_index = sorted(list(B)).index(i)
        b_hat[i] = b[i_index] - A[i_index][e_index]*b_hat[e]
        for j in N.difference({e}):
            j_index = sorted(list(N)).index(j)
            A_hat[i][j] = A[i_index][j_index] - A[i_index][e_index]*A_hat[e][j]
        A_hat[i][l] = -A[i_index][e_index]*A_hat[e][l]
    v_hat = v + c[e_index]*b_hat[e] # Computamos la funcion objetivo
    for j in N.difference({e}):
        j_index = sorted(list(N)).index(j)
        c_hat[j] = c[j_index] - c[e_index]*A_hat[e][j]
    c_hat[l] = -c[e_index]*A_hat[e][l]
    N_hat = N.difference({e}).union({l}) # Computamos los nuevos conjuntos de variables basicas y no básicas
    B_hat = B.difference({l}).union({e})
    A_hat = [list(filter(None.__ne__, row)) for row in A_hat if any(row)]
    b_hat = list(filter(None.__ne__, b_hat))
    c_hat = list(filter(None.__ne__, c_hat))
    return N_hat, B_hat, A_hat, b_hat, c_hat, v_hat

def InitializeSimplex(A, b, c):
    m = len(A) # A es una lista de longitud m de listas de longitud n
    n = len(A[0])
    if min(b) > 0: return (set(range(n)), set(range(n, m+n)), A, b, c, 0)
    c_original = c
    k = b.index(min(b))
    N, B, A, b, c, v = LtoLaux(A, b, c)
    l = n + 1 + k # ya que hay n+1 variables no básicas contando con x_0
    N, B, A, b, c, v = pivot(N, B, A, b, c, v, l, n) # intercambiamos xl con x0
    while max(c) > 0:
        delta,  x_ = [[], []]
        e_index = c.index(max(c))
        e = sorted(list(N))[e_index]
        for i in sorted(list(B)):
            i_index = sorted(list(B)).index(i)
            if A[i_index][e_index] > 0: delta.append(b[i_index]/A[i_index][e_index])
            else: delta.append(float('inf'))
        l = delta.index(min(delta))
        if delta[l] == float('inf'): return "Unbounded"
        l = sorted(list(B))[l]
        N, B, A, b, c, v = pivot(N, B, A, b, c, v, l, e)
    x_ = []
    for i in range(len(N)):
        if i in B:
            i_index = sorted(list(B)).index(i)
            x_.append(b[i_index])
        else: x_.append(0)
    if n in B: # si x_0 es una variable básica
        x_index = sorted(list(B)).index(n)
        if min(b) < 0: return "No factible"
        for e in N:
            e_index = sorted(list(N)).index(e)
            n_index = sorted(list(B)).index(n)
            if A[n_index][e_index]: break
        N, B, A, b, c, v = pivot(N, B, A, b, c, v, n, e) # Realizar un pivoteo (degenerado) para hacer  ̄x0 no b ́asico
    x_index = sorted(list(N)).index(n)
    A = [[x for i,x in enumerate(row) if i != x_index] for row in A]
    c,v = cEval(c_original, N, B, A, b, n)
    if min(b) < 0: return "No factible"
    N.remove(n)
    for x in list(N):
        if x>n:
            N.remove(x)
            N.add(x-1)
    for x in list(B):
        if x>n:
            B.remove(x)
            B.add(x-1)
    return N, B, A, b, c, v


def LtoLaux(A, b, c):
    A = [row+[-1] for row in A] # agrego la variable nueva al final en lugar de al comienzo
    c = [0]*len(b)+[-1]
    m = len(A) # A es una lista de longitud m de listas de longitud n
    n = len(A[0])
    N = set(range(n))
    B = set(range(n, m+n))
    v = 0 # la función objetivo es -x0, sin un coeficiente v
    return N, B, A, b, c, v

def cEval(c_original, N, B, A, b, n):
    c = [0]*n
    v = 0
    for i in range(n):
        if i in N: c[i]+=c_original[i]
        else:
            for j,x in enumerate(A[sorted(list(B)).index(i)]):
                c[j]+=x
            v+=b[sorted(list(B)).index(i)]*c_original[i]
    return c,v

def printSimplex(A, b, c):
    print("\nMaximizar:\n\tz =", end = " ")
    for i,coef in enumerate(c):
        print(f"({coef})x{i+1}", end = " ")
        if i<len(c)-1: print("+", end = " ")
    print("\n\nSujeto a:", end = "\n\t")
    for i,row in enumerate(A):
        for j, coef in enumerate(row):
            print(f"({coef})x{j+1}", end = " ")
            if j<len(row)-1: print("+", end = " ")
        print("<= ", b[i], end = "\n\t")
    print()

def printSimplexSolution(x_, c):
    if isinstance(x_, list):
        print("La solución es:")
        for i,x in enumerate(x_): print(f"x{i+1} = {round(x, 3)}")
        print(f"z = {round(dotProduct(x_, c), 3)}", end = "\n\n")
    else: print(x_)

def dotProduct(x, y):
    return sum(x_i*y_i for x_i, y_i in zip(x, y))

if __name__ == '__main__':
    import yaml
    simplex_dict = yaml.load(open('simplex_input.yaml', 'r'), Loader=yaml.Loader)
    for i, (A, b, c) in enumerate(zip(simplex_dict['A'], simplex_dict['b'], simplex_dict['c'])):
        print(f'\n\n=============================\nTEST {i+1}')
        printSimplex(A, b, c)
        x = simplex(A,b,c)
        printSimplexSolution(x, c)
