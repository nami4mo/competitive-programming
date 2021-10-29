n=int(input())
al=list(map(int, input().split()))
x=int(input())
x+=1
s=sum(al)

loop=x//s
rem=x-loop*s
ans=n*loop
i=0
while rem>0:
    rem-=al[i]
    i+=1
    ans+=1
print(ans)