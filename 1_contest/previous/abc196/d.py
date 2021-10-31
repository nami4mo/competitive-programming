h,w,a,b=map(int, input().split())
s=h*w
dp=[0]*(2**s)
dp[0]=1

for i in range(2**s):
    for y in range(h):
        for x in range(w):
            if x!=w-1:
                p0=w*y+x
                p1=w*y+x+1
                if i&(1<<p0)==0 and i&(1<<p1)==0:
                    dp[i+(1<<p0)+(1<<p1)]+=dp[i]
            if y!=h-1:
                p0=w*y+x
                p1=w*(y+1)+x
                if i&(1<<p0)==0 and i&(1<<p1)==0:
                    dp[i+(1<<p0)+(1<<p1)]+=dp[i]

ans=0
for i in range(2**s):
    if bin(i).count("1")==2*a:ans+=dp[i]
for i in range(1,a+1):
    ans//=i
print(ans)