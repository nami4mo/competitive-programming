n,k=map(int, input().split())
top=0

top+=(k-1)*(n-k)*6
top+=(n-1)*3
top+=1
ans=top/(n**3)
print(ans)