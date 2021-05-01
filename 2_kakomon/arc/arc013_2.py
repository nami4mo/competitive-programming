n=int(input())
ml=[0]*3
for _ in range(n):
    al=list(map(int, input().split()))
    al.sort()
    for i in range(3):
        ml[i]=max(ml[i],al[i])
ans=ml[0]*ml[1]*ml[2]
print(ans)