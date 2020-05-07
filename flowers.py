import sys

def flowers(N, k, mem):
    #mem.append(N-k+1+mem[N-k-1])
    print(f"len(mem)= {len(mem)}")
    if N>k: add = sum(mem[k-1:N-k-2])
    else: add = 0
    print(mem)
    print("add = ", add)
    try:    print(f"N= {N}\tN-k+1 = {N-k+1}.\tsum(mem[0:N-k+1]) = {sum(mem[0:N-k+1])}\tsum= {sum(mem)}")
    except: print(f"N= {N}\tN-k+1 = {N-k+1}.\t\t\tsum= {sum(mem)}")
    mem.append(N-k+1+mem[N-k-1]+add)
    print(mem); print()
    return mem

def iteration(a_list,b_list,k):
    mem = [1]*(k-1) # se considera la posibilidad en la cual todas las flores son rojas
    for N in range(k,max(b_list)+1): # solo es necesario recorrer hasta el valor más alto de b
        flowers(N, k, mem) # se va construyendo la tabla de memoización
    i = 0
    errors = (208634283, 519619920, 301591806, 658814541, 437343595, 1148691948)
    for (a, b) in zip(a_list, b_list): # se recorre sobre los intervaloes a,b de cada test
        i+=1; print(f"\n{i}.\ta//k={a//k}\tb//k={b//k}\ta= {a}\tb= {b}\tk= {k}")
        if sum(mem[a-1:b])%1000000007 in errors: print("ERROR")
        print(sum(mem[a-1:b])%1000000007) # se imprimen los resultados para cada test

a_list = []; b_list = []
for line in sys.stdin:
    line = line.rstrip().split()
    a_list.append(int(line[0]))
    b_list.append(int(line[1]))
t = a_list[0]; k = b_list[0] # la primera línea representa el número de tests y el valor de k
a_list = a_list[1:]; b_list = b_list[1:] # se elimina el primer valor de cada lista
iteration(a_list, b_list, k) # se llama a la función principal
