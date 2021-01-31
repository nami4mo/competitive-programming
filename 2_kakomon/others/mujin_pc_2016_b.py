a,b,c=map(int, input().split())
al=[a,b,c]
al.sort()
maxr=a+b+c
minr=al[2]-al[1]-al[0]
minr=max(0,minr)

PI=3.14159265359
ans=(maxr**2-minr**2)*PI
print(ans)