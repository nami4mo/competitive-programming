import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(al, n, m, all_al):
    if len(al) == n:
        all_al.append(al)
    else:
        last = al[-1]
        for i in range(last, m+1):
            dfs(al+[i], n, m, all_al)

def main():
    n, m, Q = map(int, input().split()) 
    ql = []
    for _ in range(Q):
        ql.append( list(map(int, input().split())) )

    all_al = []
    for i in range(1,m+1):
        dfs([i], n, m, all_al)

    ans = 0
    for al in all_al:
        curr_sum = 0
        for q in ql:
            if al[q[1]-1]- al[q[0]-1] == q[2]: curr_sum += q[3]
        ans = max(curr_sum, ans)

    print(ans)

if __name__ == "__main__":
    main()