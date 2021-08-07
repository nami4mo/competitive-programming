n,m,q=map(int, input().split())
gl=[[] for _ in range(n)]
gls=[]
for _ in range(m):
    a,b,s,t=map(int, input().split())
    a-=1
    b-=1
    gl[a].append((s,t,b,i))
    gls.append((a,b,s,t))

for i in range(n):
    gl[i].sort(key=lambda x:x[0])


MAX=10**10
from bisect import bisect_left, bisect_right
def find_next(gli, time):
    val=(time,MAX,-1,-1)
    ind = bisect_left(gli, val)
    ind = ind if 0 <= ind < len(gli) else None
    if ind is None:
        return -1
    else:
        return ind
    
gl_num=[-1]*n
c_num=-1
num_times=[[] for _ in range(n)]
for i in range(m):
    if gl_num[i]!=-1:continue
    
    c_num+=1
    gl_num[i]=c_num
    a,b,s,t=gls[i]
    num_times[c_num].append((s,a,b))
    num_times[c_num].append((t,b,-1))
    pos=b
    time=t
    while True:
        ind=find_next(gl[pos],time)
        if ind==-1:break
        s,t,b,gi=gl[pos][ind]
        if gl_num[gi]!=-1:
            gii=gl_num[gi]
            if 
            break
        num_times[c_num].append((s,pos,b))
        num_times[c_num].append((t,b,-1))
        pos=b
        time=t

print(num_times[:10])       