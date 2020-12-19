n=int(input())
place01 = {}
al=[]
for i in range(n):
    a=int(input())
    if i%2==0:
        place01[a] = 0
    else:
        place01[a] = 1
    al.append(a)

ans=0
al.sort()
for i in range(n):
    a=al[i]
    if place01[a] != i%2: ans+=1

print(ans//2)