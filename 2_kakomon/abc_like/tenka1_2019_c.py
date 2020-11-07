n = int(input())
s = input()

a1 = s.count('#')
a2 = s.count('.')

al = 0
al_cnts = [0]*n
ar = 0
ar_cnts = [0]*n
for i in range(n):
    if s[i] == '#': al+=1
    al_cnts[i] = al

for i in range(n-1,-1,-1):
    if s[i] == '.': ar+=1
    ar_cnts[i] = ar

ans = 10**10
for i in range(n-1):
    v = al_cnts[i] + ar_cnts[i+1]
    ans = min(ans,v)

print(min(a1,a2,ans))