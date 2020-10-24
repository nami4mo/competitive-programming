n = int(input())
divs = []
for i in range(1, int(n**0.5)+1):
    if n%i == 0:
        divs.append(i)
        if i*i != n: divs.append(n//i)

ans = 0
for d in divs:
    if d == 1: continue
    v = n
    while v%d == 0:
        v = v//d
    if v%d == 1: 
        ans+=1


divs2 = []
for i in range(1, int((n-1)**0.5)+1):
    if (n-1)%i == 0:
        divs2.append(i)
        if i*i != (n-1): divs2.append((n-1)//i)

for d in divs2:
    if d == 1: continue
    if n%d != 0: 
        ans += 1

print(ans) 