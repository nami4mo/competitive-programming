import sys
sys.setrecursionlimit(10**6)
mod = 1

def dfs1(pare, node, gl, dp, csums_l, csums_r):
    child_vl = []
    node_v = 1 # (^^)/ identity element (add/sub->0, multiple->1, ...) 
    for neib in gl[node]:
        if pare==neib: continue
        child_val = dfs1(node, neib, gl, dp, csums_l, csums_r)+1
        node_v *= child_val
        node_v %= mod
        child_vl.append(child_val)

    # left cumsums
    csums_l[node] = [1]
    lv = 1
    for cv in child_vl:
        lv*=cv
        lv%=mod
        csums_l[node].append(lv)
    # right cumsums
    csums_r[node] = [1]
    rv = 1
    for cv in child_vl[::-1]:
        rv*=cv
        rv%=mod
        csums_r[node].append(rv)

    dp[node] = node_v
    return node_v


def dfs2(pare, node, pare_v, gl, dp, csums_l, csums_r, ansl):
    ans = csums_l[node][-1]*(pare_v+1)
    ansl[node] = ans%mod

    node_n = len(gl[node])-1 if pare>=0 else len(gl[node]) # the number of the edges to children.
    child_ind = 0
    for neib in gl[node]:
        if pare==neib: continue
        node_v = csums_l[node][child_ind]*csums_r[node][node_n-child_ind-1]*(pare_v+1)
        dfs2(node, neib, node_v, gl, dp, csums_l, csums_r, ansl)
        child_ind+=1


n,m=map(int, input().split())
mod=m
gl=[[] for _ in range(n)]

for _ in range(n-1):
    u,v=map(int, input().split())
    u-=1
    v-=1
    gl[u].append(v)
    gl[v].append(u)

dp = [-1]*n
csums_l = [[] for _ in range(n)]
csums_r = [[] for _ in range(n)]
dfs1(-1,0,gl,dp,csums_l, csums_r)

ansl = [-1]*n
dfs2(-1,0,0,gl,dp,csums_l, csums_r, ansl)
for a in ansl:print(a)