n,m = map(int, input().split())

l_to_s = [0]*(m+1)
r_to_s = [0]*(m+1)
for _ in range(n):
    l,r,s = map(int, input().split())
    l_to_s[l] += s
    r_to_s[r] += s

# lrsl.sort(key=lambda x: x[1])
# lvs = [0]*(m+1)

rvs = [0]*(m+2)
csum = 0
for i in range(m+1):
    csum += r_to_s[i]
    rvs[i] = csum

lvs = [0]*(m+2)
csum = 0
for i in range(m,-1,-1):
    csum += l_to_s[i]
    lvs[i] = csum

ans = 0
for i in range(1,m+1):
    v = rvs[i-1] + lvs[i+1]
    ans = max(ans,v)

print(ans)