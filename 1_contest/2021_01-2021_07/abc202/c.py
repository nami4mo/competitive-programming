n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
cl=list(map(int, input().split()))
MAX=10**5+1
cnts=[0]*MAX
for c in cl:
    cnts[bl[c-1]]+=1

ans=0
for i in range(n):
    a=al[i]
    ans+=cnts[a]
print(ans)