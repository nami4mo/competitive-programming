ansl=[]

from itertools import permutations
n, k = 5,5 
ll = list(range(n))  # list of elements
perml = list(permutations(ll, k))

# for _ in range(int(input())):
for perm in perml:
    print('start',list(perm))
    # n=int(input())
    # pl=list(map(int, input().split()))
    # pl=[p-1 for p in pl]
    pl=list(perm)
    n=len(pl)
    if n==2:
        if pl==[0,1]:
            ansl.append([])
        else:
            ansl.append([1])
        continue

    num2i=[-1]*n
    for i in range(n):
        num2i[pl[i]]=i
    
    al=[]
    cnt=0

    if pl[0:4]==[0,3,1,2]:
        al=[1,2,1,2,1,2,1,2,1]
        cnt=9
        num2i[0]=0
        num2i[1]=2
        num2i[2]=1
        num2i[3]=3
        pl[0]=0
        pl[1]=2
        pl[2]=1
        pl[3]=3

    elif pl[0:3]==[0,3,1]:
        al=[1,2,1,2,1]
        cnt=5
        num2i[0]=0
        num2i[1]=1
        num2i[3]=2
        pl[0]=0
        pl[1]=1
        pl[2]=3

    for num in range(n):
        if num<=2 and num2i[num]<=2:continue
        if num2i[num]<=num:
            continue
        if (cnt+1)%2==num2i[num]%2:
            pass
        else:
            if num2i[num]<n-4:
                if cnt%2==n%2:
                    pl[n-1],pl[n-2]=pl[n-2],pl[n-1]
                    num2i[pl[n-1]]=n-1
                    num2i[pl[n-2]]=n-2
                    al.append(n-1)
                else:
                    pl[n-3],pl[n-2]=pl[n-2],pl[n-3]
                    num2i[pl[n-2]]=n-2
                    num2i[pl[n-3]]=n-3
                    al.append(n-2)
            else:
                if cnt%2==0:
                    pl[0],pl[1]=pl[1],pl[0]
                    num2i[pl[0]]=0
                    num2i[pl[1]]=1
                    al.append(1)
                else:
                    pl[2],pl[1]=pl[1],pl[2]
                    num2i[pl[2]]=2
                    num2i[pl[1]]=1
                    al.append(2)
            cnt+=1
        print(num,pl)
        for i in range(num2i[num],num,-1):
            pl[i-1],pl[i]=pl[i],pl[i-1]
            num2i[pl[i-1]]=i-1
            num2i[pl[i]]=i
            al.append(i)
            cnt+=1

    for i in range(3):
        if pl[i]>2:
            print(perm)
            print(pl)
            a=1/0

    tops=pl[0:3]
    while tops!=[0,1,2]:
        if cnt%2==0:
            tops[0],tops[1]=tops[1],tops[0]
            al.append(1)
            cnt+=1
        else:
            tops[1],tops[2]=tops[2],tops[1]
            al.append(2)
            cnt+=1
    ansl.append((list(perm),al))

for row in ansl:
    print(len(row))
    print(*row)