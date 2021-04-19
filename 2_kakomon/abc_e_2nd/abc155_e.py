n=input()
ln=len(n)
INF=10**18
dp_same=[INF]*(ln+1)
dp_over=[INF]*(ln+1)
dp_over[0]=1
dp_same[0]=0
for i in range(ln):
    num=int(n[i])
    dp_same[i+1]=min(dp_same[i+1], dp_same[i]+num)
    dp_same[i+1]=min(dp_same[i+1], dp_over[i]+10-num)
    dp_over[i+1]=min(dp_over[i+1], dp_same[i]+num+1)
    dp_over[i+1]=min(dp_over[i+1], dp_over[i]+10-num-1)

# ans=min(dp_same[-1],dp_over[-1])
print(dp_same[-1])