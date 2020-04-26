import sys

def flowers(N, k, mem):
    mem.append(N-k+1+mem[N-k-1])
    return mem

def iteration(a_list,b_list,k):
    mem = [1 for i in range(k-1)]
    for N in range(k,max(b_list)+1):
        flowers(N, k, mem)
    for (a, b) in zip(a_list, b_list):
        print(sum(mem[a-1:b]))

a_list = []; b_list = []
for line in sys.stdin:
    line = line.rstrip().split()
    a_list.append(int(line[0]))
    b_list.append(int(line[1]))
t = a_list[0]; k = b_list[0]
a_list = a_list[1:]; b_list = b_list[1:]
iteration(a_list, b_list, k)
