a,b,c=map(int, input().split())
ans=10**18

aa=b-(c-b)
v=aa-a
if v>=0:ans=min(ans,v)

cc=b+(b-a)
v=cc-c
if v>=0:ans=min(ans,v)

vv=0
if (a+c)%2!=0: 
    c+=1
    vv=1
    
bb=(a+c)//2
v=bb-b
if v>=0:ans=min(ans,v+vv)

print(ans)