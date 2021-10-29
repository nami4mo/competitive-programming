s=input()
vp=0
vm=0
al=[]
for si in s:
    if si=='+':
        vp+=1
    elif si=='-':
        vm+=1
    else:
        al.append(vp-vm)
al.sort(reverse=True)
n=len(al)
ans=sum(al[:n//2])-sum(al[n//2:])
print(ans)