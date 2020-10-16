n = int(input())

divs = []
for i in range(1, int(n**0.5)+1):
    if n%i == 0:
        divs.append(i)
        if i*i != n: divs.append(n//i)
# print(divs)
ans = 0
for d in divs:
    d-=1
    if d==0: continue
    a = n//d
    rem = n%d
    # print(d,a,rem)
    if a==rem: ans += d

print(ans)