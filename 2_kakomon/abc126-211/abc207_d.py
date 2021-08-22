from math import degrees,atan2

eps=10**(-8)
def check(n,s_da,t_da):
    for start in range(n-1):
        new_s_da=[]
        for i in range(n-1):
            ind=(start+i)%(n-1)
            new_s_da.append(s_da[ind])
        offset=new_s_da[0][0]
        for i in range(n-1):
            new_s_da[i]=((new_s_da[i][0]-offset)%360, new_s_da[i][1])
        for i in range(n-1):
            a1,d1=new_s_da[i]
            a2,d2=t_da[i]
            if abs(a1-a2)>eps or d1!=d2:
                break
        else:
            return True
    return False


def get_da(n, center_ind, abl):
    res=[]
    cx,cy=abl[center_ind]
    for i in range(n):
        if i==center_ind:continue
        x,y=abl[i]
        d2=(cx-x)**2+(cy-y)**2
        angle=degrees(atan2(y-cy,x-cx))
        res.append((angle,d2))
    res.sort()
    mina=res[0][0]
    for i in range(n-1):
        res[i]=(res[i][0]-mina, res[i][1])
    return res

n=int(input())
if n==1:
    print('Yes')
    exit()

abl=[]
cdl=[]
for _ in range(n):
    a,b=map(int, input().split())
    abl.append((a,b))
for _ in range(n):
    c,d=map(int, input().split())
    cdl.append((c,d))

t_da=get_da(n,0,cdl)
for i in range(n):
    s_da=get_da(n,i,abl)
    if check(n, s_da, t_da):
        print('Yes')
        exit()
print('No')
