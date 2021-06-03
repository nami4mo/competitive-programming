ansl=[]

from itertools import permutations
n, k = 6,6 
ll = list(range(n))  # list of elements
perml = list(permutations(ll, k))


for _ in range(int(input())):
    n=int(input())
    pl=list(map(int, input().split()))
    pl=[p-1 for p in pl]
# for perm in perml:
#     pl=list(perm)
#     n=len(pl)

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

    for num in range(n-1,4-1,-1):
        if num2i[num]==num:continue
        ind=num2i[num]
        if (cnt)%2!=num2i[num]%2:
            if cnt%2==0:
                d=0
                if pl[1]==num:d+=2
                pl[0+d],pl[1+d]=pl[1+d],pl[0+d]
                num2i[pl[0+d]]=0+d
                num2i[pl[1+d]]=1+d
                al.append(1+d)
                cnt+=1
            else:
                d=0
                if pl[2]==num:d+=2
                pl[2+d],pl[1+d]=pl[1+d],pl[2+d]
                num2i[pl[2+d]]=2+d
                num2i[pl[1+d]]=1+d
                al.append(2+d)  
                cnt+=1
        for i in range(num2i[num],num):
            pl[i+1],pl[i]=pl[i],pl[i+1]
            num2i[pl[i+1]]=i+1
            num2i[pl[i]]=i
            al.append(i+1)
            cnt+=1
    # print(pl)
    if n>=4:
        num=3
        if (cnt)%2!=num2i[num]%2:
            ind=num2i[num]
            if ind==0:
                pl[2],pl[1]=pl[1],pl[2]
                num2i[pl[2]]=2
                num2i[pl[1]]=1
                al.append(2)  
                cnt+=1
            elif ind==1:
                pl[2],pl[3]=pl[3],pl[2]
                num2i[pl[2]]=2
                num2i[pl[3]]=3
                al.append(3)  
                cnt+=1
            elif ind==2:
                pl[1],pl[2],pl[3]=pl[3],pl[1],pl[2]
                num2i[pl[1]]=1
                num2i[pl[2]]=2
                num2i[pl[3]]=3
                al.extend([2,3,2,3])  
                cnt+=4
        for i in range(num2i[num],num):
            pl[i+1],pl[i]=pl[i],pl[i+1]
            num2i[pl[i+1]]=i+1
            num2i[pl[i]]=i
            al.append(i+1)
            cnt+=1
    # print(pl,cnt)
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
    ansl.append(al)
    # ansl.append((list(perm),al))

# for ppl,al in ansl:
#     pl=ppl[:]
#     print(ppl,al)
#     for i,a in enumerate(al):
#         a-=1
#         pl[a],pl[a+1]=pl[a+1],pl[a]
#         if (a)%2!=i%2:
#             print(ppl,al,"aaa")
#             break
#     if pl!=[0,1,2,3,4,5]:
#         print(ppl,"bbb")
#         break
for row in ansl:
    print(len(row))
    print(*row)