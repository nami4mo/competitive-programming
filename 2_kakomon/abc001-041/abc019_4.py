n=int(input())

maxi,maxd=-1,-1
for i in range(2,n+1):
    print('?',1,i,flush=True)
    d=int(input())
    if d>maxd:
        maxi,maxd=i,d

ans=0
for i in range(1,n+1):
    print('?',maxi,i,flush=True)
    d=int(input())
    ans=max(ans,d)
print('!',ans)