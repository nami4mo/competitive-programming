n=int(input())
ans=0
for i in range(1,n+1):
    if '7' in str(i): continue
    oc = str(oct(i))[2:]
    if '7' in oc: continue
    ans+=1

print(ans)