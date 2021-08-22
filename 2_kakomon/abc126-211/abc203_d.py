n,k=map(int, input().split())
al=[list(map(int, input().split())) for _ in range(n)]

if k==1:
    ans=10**9
    for row in al:
        ans=min(min(row),ans)
    print(ans)
    exit() 

def check(al,mid):
    bl=[]
    for row in al:
        brow=[1 if a<=mid else 0 for a in row]
        bl.append(brow)

    csums = [ [0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            csums[i+1][j+1] = csums[i+1][j] + csums[i][j+1] - csums[i][j] + bl[i][j]
    
    kcnt=k**2-((k**2)//2)
    # print(kcnt,kcnt)
    for y in range(n-k+1):
        for x in range(n-k+1):
            cnt=csums[y+k][x+k]-csums[y][x+k]-csums[y+k][x]+csums[y][x]
            if cnt>=kcnt:return True
    return False


ng, ok = -1, 10**9+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    # ...
    if check(al,mid): ok = mid
    else: ng = mid
print(ok)