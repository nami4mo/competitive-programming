n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
cl=list(map(int, input().split()))

aa=[0]*46
bb=[0]*46
cc=[0]*46
for i in range(n):
    aa[al[i]%46]+=1
    bb[bl[i]%46]+=1
    cc[cl[i]%46]+=1

ans=0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46==0: ans+=aa[i]*bb[j]*cc[k]
print(ans)