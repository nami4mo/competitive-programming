n=int(input())
pl=list(map(int, input().split()))
ql=[-1]*n
for i in range(n):
    ql[pl[i]-1]=i+1
print(*ql)