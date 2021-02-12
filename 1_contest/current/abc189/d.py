n=int(input())
sl=[input() for _ in range(n)]

dpt=[0]*(n+1)
dpf=[0]*(n+1)
dpt[0]=1
dpf[0]=1

for i in range(n):
    s=sl[i]
    if s=='AND':
        dpf[i+1]=dpf[i]*2+dpt[i]
        dpt[i+1]=dpt[i]
    else:
        dpf[i+1]=dpf[i]
        dpt[i+1]=dpf[i]+dpt[i]*2

print(dpt[-1])
