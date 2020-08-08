n = int(input())
s = str(input())

MOD = 10**9 + 7
s_d = {}
for curr_s in s:
    s_d.setdefault(curr_s,0)
    s_d[curr_s] += 1

ans = 1
for k,v in s_d.items():
    ans *= (v+1)
    ans%=MOD
ans-=1
ans%=MOD
print(ans)