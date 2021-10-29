al=[list(map(int, input().split())) for _ in range(5)]
used=[False]*25
first_used=[[False]*5 for _ in range(5)]
fixed=[(-1,-1)]*25
rems=[]
i2yx=[]
yx2i={}
for i in range(5):
    for j in range(5):
        al[i][j]-=1
        if al[i][j]!=-1:
            used[al[i][j]]=True
            fixed[al[i][j]]=(i,j)
            first_used[i][j]=True
        else:
            i2yx.append((i,j))
            yx2i[(i,j)]=len(i2yx)-1

for i in range(25):
    if used[i]:continue
    rems.append(i)
# print(i2yx)



MAX=len(rems)
lens=[[] for _ in range(MAX+1)]
for i in range(1<<MAX):
    x=bin(i).count("1")
    lens[x].append(i)

board=[[False]*5 for _ in range(5)]
def check_used(y,x,bits):
    if board[y][x]:return True
    if (y,x) in yx2i:
        ind=yx2i[(y,x)]
        if bits&(1<<ind):return True
    return False

def check_ok_yoko(y,x,bits):
    if x==0 or x==4: return True
    if check_used(y,x-1,bits)^check_used(y,x+1,bits):return False
    return True

def check_ok_tate(y,x,bits):
    if y==0 or y==4: return True
    if check_used(y-1,x,bits)^check_used(y+1,x,bits):return False
    return True

dp=[0]*(1<<MAX)
dp[0]=1
prev_num=0
for cnt in range(MAX):
    num=rems[cnt]
    for i in range(prev_num,num):
        # print('put',i)
        y,x=fixed[i]
        for bits in lens[cnt]:
            if (not check_ok_yoko(y,x,bits)) or (not check_ok_tate(y,x,bits)):
                dp[bits]=0
        board[y][x]=True
    prev_num=num+1
    for bits in lens[cnt]:
        for y in range(5):
            for x in range(5):
                if check_used(y,x,bits):continue
                if first_used[y][x]:continue
                yxi=1<<yx2i[(y,x)]
                if check_ok_yoko(y,x,bits) and check_ok_tate(y,x,bits):
                    dp[bits|yxi]+=dp[bits]
                    # print(bits, bits|yxi)
    # print(num+1,dp)

# for i in range(1<<MAX):
print(dp[-1])