n=int(input())
d=[0]*200
al=list(map(int, input().split()))
for a in al:
    d[a%200]+=1

ans=0
for v in d:
    ans+=v*(v-1)//2 
print(ans)