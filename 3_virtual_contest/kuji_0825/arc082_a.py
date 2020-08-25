n = int(input())
al = list(map(int, input().split()))    
# al.sort()
al_cnts = [0]*(10**5+1)
for a in al:
    al_cnts[a] += 1

ans = 0
for a1,a2,a3 in zip(al_cnts[0:-2],al_cnts[1:-1],al_cnts[2:]):
    v = a1+a2+a3
    ans = max(ans,v)

print(ans)