n,m=map(int, input().split())
al=[0]*n
for i in range(n):
    al[i]=n-i

for i in range(m):
    a=int(input())
    a-=1
    al[a]=i+n+1

vl=[]
for i,a in enumerate(al):
    vl.append((a,i+1))

vl.sort(reverse=True)
for _,i in vl:print(i)