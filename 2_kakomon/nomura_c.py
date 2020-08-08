import math

def main():
    n = int(input())
    A = list(map(int, input().split()))

    if A[0] != 0:
        print(-1)
        return 

    limit_v = [0]*(n+1)
    limit_v[0] = 1
    for i in range(1, n+1):
        curr_limit_v = (limit_v[i-1] - A[i-1])*2
        limit_v[i] = curr_limit_v


    v_cnt = [0]*(n+1)
    v_cnt[n] = min(limit_v[n], A[n])
    ans = 0
    for i in range(n-1,0,-1):
        leaf = A[i]
        max_not_leaf = v_cnt[i+1]
        min_not_leaf = v_cnt[i+1]//2 + v_cnt[i+1]%2

        curr_max_v = max_not_leaf + leaf
        curr_min_v = min_not_leaf + leaf

        if limit_v[i] < curr_min_v:
            print(-1)
            return

        v_cnt[i] = min(limit_v[i], curr_max_v)

    v_cnt[0] = 1
    ans = sum(v_cnt)
    if ans == 0: 
        ans = -1
    print(ans)

if __name__ == "__main__":
    main()