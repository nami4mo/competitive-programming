import sys
sys.setrecursionlimit(10**6)

MOD = 10**9+7

def dfs(h,w,hi,wi,dp,al):
    if dp[hi][wi] != -1:
        return dp[hi][wi]
    v = 1
    pos_v = al[hi][wi]
    for dh,dw in [[-1,0],[1,0],[0,-1],[0,1]]:
        nh,nw = hi+dh, wi+dw
        if not 0 <= nh < h: continue
        if not 0 <= nw < w: continue
        if pos_v >= al[nh][nw]: continue
        v += dfs(h,w,nh,nw,dp,al)
    v %= MOD
    dp[hi][wi] = v
    return v


def main():
    h,w = map(int, input().split())
    al = [list(map(int, input().split())) for _ in range(h)]
    dp = [ [-1]*w for _ in range(h) ]

    ans = 0
    for i in range(h):
        for j in range(w):
            ans += dfs(h,w,i,j,dp,al)
    print(ans%MOD)
    # print(dp)

if __name__ == "__main__":
    main()