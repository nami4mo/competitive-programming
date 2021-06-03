n=int(input())
aal=list(map(int, input().split()))
ail=[]
for a in aal:
    if (not ail) or ail[-1][0]!=a: 
        ail.append((a,len(ail)))

n=len(ail)
ail.sort(reverse=True)
land=[False]*(n+1) # -1 -> n

ans=0
cnt=0
prev=-1
for a,i in ail:
    if prev!=a: ans=max(ans,cnt)

    if a==0:break
    if not (land[i-1] or land[i+1]):
        cnt+=1
    elif land[i-1] and land[i+1]:
        cnt-=1
    else:
        pass
    land[i]=True
    prev=a

ans=max(ans,cnt)
print(ans)