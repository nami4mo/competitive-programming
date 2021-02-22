ansl=[]
for _ in range(int(input())):
    n,k=map(int, input().split())
    al=list(map(int, input().split()))
    lastk=0
    for i in range(k):
        for j in range(n-1):
            if al[j]<al[j+1]:
                al[j]+=1
                lastk=j+1
                break
        else:
            lastk=-1
            break
    ansl.append(lastk)
for a in ansl:print(a)