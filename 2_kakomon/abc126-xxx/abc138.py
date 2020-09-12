import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, q = map(int, input().split())
g = [ [] for _ in range(n) ]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

pl = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    pl[p-1] += x


def dfs(curr, pare):
    for chi in g[curr]:
        if chi == pare: continue
        pl[chi] += pl[curr]
        dfs(chi, curr)

def main():
    dfs(0,-1)
    print(*pl)

if __name__ == "__main__":
    main()