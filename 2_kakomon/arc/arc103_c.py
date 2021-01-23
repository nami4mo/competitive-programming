s=list(input())
n=len(s)
s=['0']+s
if s[n]=='1' or s[1]=='0' or s[n-1]=='0':
    print(-1)
    exit()
for i in range(1,n//2+1):
    if s[i]!=s[n-i]:
        print(-1)
        exit()

s[-1]='1'
cnts=[]
curr_x=0
for si in s[2:]:
    if si=='0':
        curr_x+=1
    else:
        cnts.append(curr_x)
        curr_x=0

lastu=1
nextu=2
ansl=[]
for cnt in cnts:
    ansl.append((lastu,nextu))
    pare=nextu
    lastu=pare
    nextu+=1
    for i in range(cnt):
        ansl.append((pare,nextu))
        nextu+=1
    
for u,v in ansl:print(u,v)