sl=[input() for _ in range(3)]
v=list(input())
ans=''
for vi in v:
    vi=int(vi)-1
    ans+=sl[vi]
print(ans)