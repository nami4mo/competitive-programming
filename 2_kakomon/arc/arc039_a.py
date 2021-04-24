a,b=map(str, input().split())
v=-10**10

for i in range(3):
    v1=int(a[:i]+'9'+a[i+1:])-int(b)
    v=max(v,v1)

for i in range(3):
    c='0'
    if i==0:c='1'
    v1=int(a)-int(b[:i]+c+b[i+1:])
    v=max(v,v1)
print(v)