n=int(input())
al=[]
for _ in range(n):
    s,t=map(str, input().split())
    t=int(t)
    al.append((t,s))

al.sort(reverse=True)
print(al[1][1])