n=int(input())
vl=[]
for _ in range(n):
    vl.append((int(input()),'a'))
for _ in range(n):
    vl.append((int(input()),'b'))

vl.sort(key=lambda x:x[0])
# print(vl)
ans=1
MOD=10**9+7
cnt=0
for v,ab in vl:
    if ab=='a':
        if cnt<0:ans*=abs(cnt)
        cnt+=1
    else:
        if cnt>0:ans*=cnt
        cnt-=1
    ans%=MOD
print(ans)