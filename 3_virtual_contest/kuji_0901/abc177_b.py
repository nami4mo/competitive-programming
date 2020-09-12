s=input()
t=input()
n = len(s)
ans = 10**9
for i in range(n):
    v = 0
    for j in range(len(t)):
        if j+i >= n: break
        if s[j+i] != t[j]: v+=1
    else:
        ans = min(ans,v)

print(ans)