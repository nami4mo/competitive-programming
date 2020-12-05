n=int(input())

downs=[]
zeros=[]
ups=[]

for _ in range(n):
    a,b = map(int, input().split())
    if a<b:
        downs.append((a,b))
    elif a>b:
        ups.append((a,b))
    else:
        zeros.append((a,b))

downs.sort(key=lambda x: x[0])
ups.sort(key=lambda x: -x[1])

abl = downs+zeros+ups

ans = 0
v = 0
for a,b in abl:
    v+=a
    ans=max(v,ans)
    v-=b

print(ans)