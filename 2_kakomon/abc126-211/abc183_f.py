from functools import lru_cache

@lru_cache(None)
def rec(price, used_cnt):
    if used_cnt>=len(al):
        return 1
    if used_cnt==len(al)-1:
        return 1

    coin=al[used_cnt]
    next_coin=al[used_cnt+1]
    rem=price%next_coin
    res=0
    if rem!=0:
        res+=rec(price-rem,used_cnt+1)
        res+=rec(price+(next_coin-rem),used_cnt+1)
    else:
        res+=rec(price,used_cnt+1)
    return res

n,x=map(int, input().split())
al=list(map(int, input().split()))
ans=rec(x,0)
print(ans)