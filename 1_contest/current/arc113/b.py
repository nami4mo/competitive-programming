a,b,c=map(int, input().split())
loops=[
    1,
    1,
    4,
    4,
    2,
    1,
    1,
    4,
    4,
    2
]

a0=a%10
mod=loops[a0]
if mod==1:
    print(a0)
    exit()

bc=pow(b,c,mod)
if bc==0: bc=mod
ans=pow(a,bc,10)
print(ans)