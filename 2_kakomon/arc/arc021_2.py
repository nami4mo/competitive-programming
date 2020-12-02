n=int(input())
bl=[int(input()) for _ in range(n)]
al=[0]
cb = 0
for i in range(n-1):
    cb ^= bl[i]
    al.append(cb)

if al[0]^al[-1] == bl[-1]:
    for a in al:print(a)

else:
    print(-1)