n=int(input())
s=input()

ans=0
for i in range(0,1000):
    istr=str(i).zfill(3)
    pos=0
    for si in s:
        if si==istr[pos]:
            pos+=1
        if pos==3:
            ans+=1
            break
print(ans)