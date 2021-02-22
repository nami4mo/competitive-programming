ansl=[]
for _ in range(int(input())):
    n=int(input())
    max2b_1=2*n-1
    max_root=int(max2b_1**0.5)
    ans=(max_root-1)//2
    ansl.append(ans)
for a in ansl:print(a)