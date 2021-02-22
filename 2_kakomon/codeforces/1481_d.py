import sys
input = sys.stdin.readline
ansl=[]
for _ in range(int(input())):
    n,k=map(int, input().split())
    sl=[]
    for _ in range(n):
        sl.append(list(input()))

    if n==2:
        if k%2==1 or sl[0][1]==sl[1][0]:
            ansl.append([1,2]*((k-1)//2+1))
            if k%2==0:ansl[-1].append(1)
        else: 
            ansl.append([])
        continue

    ans=[]
    if k%2==1:
        ans.extend([1,2]*(k//2+1))
        ansl.append(ans)
        continue
    if sl[0][1]==sl[1][0]:
        ans.extend([1,2]*(k//2))
        ans.append(1)
        ansl.append(ans)
        continue
    if sl[1][2]==sl[2][1]:
        ans.extend([2,3]*(k//2))
        ans.append(2)
        ansl.append(ans)
        continue
    if sl[2][0]==sl[0][2]:
        ans.extend([3,1]*(k//2))
        ans.append(3)
        ansl.append(ans)
        continue
    if sl[0][1]==sl[1][2] and sl[1][2]==sl[2][0]:
        for i in range(k+1):
            ans.append((i%3)+1)
        ansl.append(ans)
        continue
    abi=-1
    aai=-1
    bbi=-1
    for i in range(3):
        if sl[i][(i+1)%3]=='a' and sl[i][(i+2)%3]=='a':
            aai=i+1
        elif sl[i][(i+1)%3]=='b' and sl[i][(i+2)%3]=='b':
            bbi=i+1
        else:
            abi=i+1
    if k%4==0:
        ans.extend([abi,aai]*(k//4))
        ans.extend([abi,bbi]*(k//4))
        ans.append(abi)
    else:
        loop=(k//2)//2+1
        ans.extend([aai,abi]*loop)
        ans.extend([bbi,abi]*loop)
        ans=ans[:-1]
    ansl.append(ans)
    
for row in ansl:
    if row:
        print('YES')
        print(*row)
    else:
        print('NO')
