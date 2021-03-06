n=int(input())
al=[]
bl=[]
for _ in range(n):
    a,b=map(int, input().split())
    # abl.append((a,b))
    al.append(a)
    bl.append(b)

ans=10**10
for i in range(n):
    for j in range(n):
        if i==j: ans=min(ans,al[i]+bl[j])
        else:
            t=max(al[i],bl[j])
            ans=min(ans,t)
print(ans)

# ans2=10**10
# for a,b in abl:
#     ans2=min(ans2,a+b)

# amin=10**10
# amin2=False
# bmin=10**10
# bmin2
