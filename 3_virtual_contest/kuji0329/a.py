a,b,c,d,k=map(int, input().split())
m1=a*60+b
m2=c*60+d
ans=m2-m1-k
ans=max(0,ans)
print(ans)