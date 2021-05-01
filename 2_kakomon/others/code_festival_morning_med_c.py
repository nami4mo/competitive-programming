p,n=map(str, input().split())
p=float(p)
n=int(n)
if p>=1.0:
    if n%2==0:
        print(0)
    else:
        print(1)
    exit()
ans=-pow(1-2*p,n)/2+0.5
print(ans)