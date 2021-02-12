n,k=map(int, input().split())
al=list(map(int, input().split()))
cnts=[0]*(4*10**5)

for a in al:
    cnts[a]+=1

ans=0
boxk=k
for i in range(3*10**5+1):
    if cnts[i]==0:break
    icnt=min(cnts[i],boxk)
    ans+=icnt
    boxk=icnt

print(ans)