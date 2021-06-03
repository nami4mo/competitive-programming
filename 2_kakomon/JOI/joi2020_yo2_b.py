n=int(input())
atl=[(0,0)]
for _ in range(n):
    a,t=map(int, input().split())
    atl.append((a,t))

atl.sort(reverse=True)
# print(atl)
a,t=atl[0]
ct=max(a,t)
prev_a=a
for a,t in atl[1:]:
    d=prev_a-a
    t1=ct+d
    ct=max(t1,t)
    prev_a=a
print(ct)
