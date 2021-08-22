x,y,a,b=map(int, input().split())
ans=0
while x*a<x+b and x*a<y:
    x*=a
    ans+=1

rem=y-x-1
ans+=max(0,rem//b)
print(ans)