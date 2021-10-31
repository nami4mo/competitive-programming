n=int(input())
k=int(input())
sl=[input() for _ in range(n)]
sll=[]
st=set()
for i in range(n**2):
    y=i//n
    x=i%n
    if sl[y][x]=='.':
        sll.append(True)
        st.add(1<<i)
    else:
        sll.append(False)


def i2pos(i):
    y=i//n
    x=i%n
    return y,x
    
p2=[1<<i for i in range(64)]
def check_neib(y,x,dy,dx):
    yy=y+dy
    xx=x+dx
    if not (0<=yy<n and 0<=xx<n): return -1
    if sl[yy][xx]=='#': return -1
    return p2[yy*n+xx]

for ki in range(2,k+1):
    new_st=set()
    for v in st:
        for i in range(n**2):
            if v&(1<<i):
                y,x=i2pos(i)
                for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                    res=check_neib(y,x,dy,dx)
                    if res==-1:continue
                    new_val=v|res 
                    if new_val in st:continue
                    new_st.add(new_val)
    st=new_st
print(len(st))
                