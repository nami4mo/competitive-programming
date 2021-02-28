ansl=[]
for _ in range(int(input())):
    al=list(map(int, input().split()))
    s=sum(al)
    if s%9!=0:
        ansl.append('NO')
        continue
    if min(al)<s//9:
        ansl.append('NO')
    else:
        ansl.append('YES')
for a in ansl:print(a) 