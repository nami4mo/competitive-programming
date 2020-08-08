import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(curr, pare, pare_c, k, color_dic):
    curr_c = pare_c
    for chi in g[curr]:
        if chi == pare: continue
        curr_c = curr_c%k + 1
        color_dic[(curr,chi)] = curr_c
        dfs(chi, curr, curr_c, k, color_dic)


n = int(input())
g = [ [] for _ in range(n+1)]
gl = []
for i in range(n-1):
    a, b = map(int, input().split()) 
    g[a].append(b)
    g[b].append(a)
    gl.append((a,b))


k = 0
for node in g:
    k = max(len(node),k)


color_dic = {}
dfs(1, -1, 0, k, color_dic)

print(k)
for edge in gl:
    print(color_dic[edge])