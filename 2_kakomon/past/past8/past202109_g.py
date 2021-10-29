
def main():
    n,k=map(int, input().split())
    abcl=[]
    for _ in range(n):
        a,b,c=map(int, input().split())
        abcl.append((a,b,c))
    ng, ok = -1, 10**18+1
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        cnt=0
        for a,b,c in abcl:
            v=(mid-b)//c+1
            v=max(0,v)
            v=min(v,a)
            cnt+=v
        # ...
        if cnt>=k:
            ok = mid
        else:
            ng = mid
    print(ok)        


if __name__ == '__main__':
    main()