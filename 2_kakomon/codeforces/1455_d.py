ansl=[]
for _ in range(int(input())):
    n,x=map(int, input().split())
    al=list(map(int, input().split()))
    ans=0
    for j in range(n-1):
        if al[j]>al[j+1]:
            break
    else:
        ansl.append(0)
        continue
    for i in range(n):
        if x<al[i]:
            x,al[i]=al[i],x
            ans+=1
        for j in range(n-1):
            if al[j]>al[j+1]:
                break
        else:
            ansl.append(ans)
            break
    else:
        ansl.append(-1)
for a in ansl:print(a)