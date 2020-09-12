n,k = map(int, input().split())
xl = list(map(int, input().split())) 

xlm = []
xlp = []
for x in xl:
    if x < 0: xlm.append(x*(-1))
    elif x == 0: k-=1
    else: xlp.append(x)

xlm.sort()
ans = 10**9
for i in range(min(k,len(xlm))+1):
    if i == 0: lv = 0
    else: lv = xlm[i-1]
    
    rem = k-i
    if rem > len(xlp): continue
    if rem == 0: rv = 0
    else: rv = xlp[rem-1]
    v = lv*2+rv
    ans = min(ans,v)

for i in range(min(k,len(xlp))+1):
    if i == 0: rv = 0
    else: rv = xlp[i-1]
    
    rem = k-i
    if rem > len(xlm): continue
    if rem == 0: lv = 0
    else: lv = xlm[rem-1]
    v = lv+rv*2
    ans = min(ans,v)

print(ans)