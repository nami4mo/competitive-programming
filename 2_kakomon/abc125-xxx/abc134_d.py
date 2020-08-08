N = int(input())
al = list(map(int, input().split()))

al = [0] + al # 1-index
multi_cnts = [0]*(N+1)
ans = []
for n in range(N,0,-1):
    if multi_cnts[n] != al[n]:
        ans.append(n)
        for i in range(1, int(n**0.5)+1):
            if n%i == 0:
                multi_cnts[i]+=1
                multi_cnts[i]%=2
                if i*i != n:
                    multi_cnts[n//i]+=1
                    multi_cnts[n//i]%=2


print(len(ans))
if ans: print(*ans)