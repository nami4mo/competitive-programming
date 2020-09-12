from itertools import product
import math

D, G = map(int, input().split()) 
ipcl = []
for i in range(D):
    p, c = map(int, input().split()) 
    ipcl.append( [i+1, p, c] )

pattern = 2
ite = product(range(pattern),repeat=D)

ans = 10**5
for comb in ite:

    curr_ipcl = ipcl[:]
    curr_sum = 0
    curr_prob = 0
    for i, comp in enumerate(comb):
        if comp:
            pi, p,c = ipcl[i]
            curr_sum += (i+1)*p*100
            curr_sum += c
            curr_prob += p
            curr_ipcl[i] = [pi,0,0]
    
    for ipc in reversed(curr_ipcl):
        i,p,c = ipc
        if curr_sum + p*i*100 <= G:
            curr_sum += p*i*100
            curr_prob += p
        else:
            remain = max(0, G-curr_sum)
            curr_prob += math.ceil( remain/(i*100) )
            break

    ans = min(ans, curr_prob)


print(ans)