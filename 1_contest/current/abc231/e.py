from functools import lru_cache

al=[]

@lru_cache(None)
def rec(price, used_cnt):
    if used_cnt>=len(al):
        return 1
    if price==0:
        return 0
    if used_cnt==len(al)-1:
        return price//al[used_cnt]
 
    coin=al[used_cnt]
    next_coin=al[used_cnt+1]
    rem=price%next_coin
    cnt=rem//coin

    res=10**10
    if rem!=0:
        res=min(res, rec(price-rem, used_cnt+1)+cnt) # use 
        res=min(res, rec(price+(next_coin-rem), used_cnt+1)+ (next_coin-rem)//coin ) #nouse
    else:
        res=min(res, rec(price,used_cnt+1))

    return res


def main():
    global al
    n,x=map(int, input().split())
    al=list(map(int, input().split()))
    ans=rec(x,0)
    print(ans)


if __name__ == "__main__":
    main()