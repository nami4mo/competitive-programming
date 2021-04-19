l=input()
n=len(l)
same=1
small=0
MOD=10**9+7
for li in l:
    if li=='1':
        small=small*3+same
        same=same*2
    else:
        # same=same
        small=small*3
    small%=MOD
    same%=MOD
ans=(small+same)%MOD
print(ans)