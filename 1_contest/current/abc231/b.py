n=int(input())
d={}
for _ in range(n):
    s=input()
    d.setdefault(s,0)
    d[s]+=1

d=list(d.items())
d.sort(key=lambda x:x[1])
print(d[-1][0])
