n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
a=max(al)
b=min(bl)
cnt=b-a+1
cnt=max(0,cnt)
print(cnt)