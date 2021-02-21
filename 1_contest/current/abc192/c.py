n,k=map(int, input().split())
v=n
for i in range(k):
    vs=list(str(v))
    vs.sort()
    vs2=''.join(vs)
    vs1=vs2[::-1]
    v2=int(vs2)
    v1=int(vs1)
    v=v1-v2
    # print(v1,v2,v)
print(v)