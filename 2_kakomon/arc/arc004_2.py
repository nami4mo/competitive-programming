n=int(input())
al=[int(input()) for _ in range(n)]
al.sort()
s=sum(al)
m=al[-1]-sum(al[:-1])
m=max(m,0)
print(s)
print(m)