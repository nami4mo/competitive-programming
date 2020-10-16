h,w = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]

ansl = []
for i in range(h):
    for j in range(w-1):
        if al[i][j]%2 == 1:
            al[i][j]-=1
            al[i][j+1]+=1
            ansl.append((i+1,j+1,i+1,j+2))

for i in range(h-1):
    if al[i][-1]%2 == 1:
        al[i][-1]-=1
        al[i+1][-1]+=1
        ansl.append((i+1,w,i+2,w))

print(len(ansl))
for v in ansl:
    print(*v)