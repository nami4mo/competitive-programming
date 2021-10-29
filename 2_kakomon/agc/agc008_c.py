al=list(map(int, input().split())) # I O T J L

ans=al[1]*2

ans2=0
ans2+=(al[0]//2)*4
ans2+=(al[3]//2)*4
ans2+=(al[4]//2)*4

ans3=0
if min(al[0],al[3],al[4])>=1:
    al[0]-=1
    al[3]-=1
    al[4]-=1
    ans3+=6
    ans3+=(al[0]//2)*4
    ans3+=(al[3]//2)*4
    ans3+=(al[4]//2)*4

ans+=max(ans2,ans3)
print(ans//2)
