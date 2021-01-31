n=int(input())
al=list(map(int, input().split()))
ans=0
cnt=0
last=-1
for a in al:
    if a>last:
        last=a
        cnt+=1
    else:
        ans+=(cnt+1)*cnt//2
        cnt=1
        last=a
ans+=(cnt+1)*cnt//2
print(ans)
