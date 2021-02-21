n=int(input())

if n==3:
    print(2,5,63)
    exit()

if n==5:
    print(2,3,4,9,12)
    exit()

al=[]
for i in range(n):
    if i%4==0: al.append(6*(i//4)+2)
    if i%4==1: al.append(6*(i//4)+3)
    if i%4==2: al.append(6*(i//4)+4)
    if i%4==3: al.append(6*(i//4)+6)

s=sum(al)
if s%6==2:
    for i in range(n-1,-1,-1):
        if al[i]%6==0:
            al[i]+=4
            break

elif s%6==5:
    for i in range(n-1,-1,-1):
        if al[i]%6==3:
            al[i]+=7
            break

elif s%6==3:
    for i in range(n-1,-1,-1):
        if al[i]%6==0:
            al[i]+=3
            break
        if al[i]%6==3:
            al[i]+=3
            break

print(*al)