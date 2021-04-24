n,a,b=map(int, input().split())
al=list(map(int, input().split()))
al.sort()

if a==1:
    al.sort()
    for ans in al:print(ans)
    exit()

while True:
    al[0]*=a
    al.sort()
    b-=1
    for i in range(n-1):
        if al[i]*a<al[-1]:
            break
    else:
        break
    if b==0:break

MOD=10**9+7
rem=b%n
ls=[]
rs=[]
for i in range(n):
    if i<rem:
        cnt=b//n+1
        v=al[i]*pow(a,cnt,MOD)
        rs.append(v%MOD)
    else:
        cnt=b//n
        v=al[i]*pow(a,cnt,MOD)
        ls.append(v%MOD)      
for ans in ls+rs:print(ans)
