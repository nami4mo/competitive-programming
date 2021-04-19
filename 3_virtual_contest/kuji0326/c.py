n=int(input())
al=list(map(int, input().split()))
al.sort()
cnt={}
for a in al:
    cnt.setdefault(a,0)
    cnt[a]+=1

ans=0
for k,v in cnt.items():
    if k>v:ans+=v
    else: ans+=(v-k)
print(ans)