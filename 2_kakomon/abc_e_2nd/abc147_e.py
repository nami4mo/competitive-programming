h,w=map(int, input().split())
def pos(y,x):
    return y*w+x

al=[ list(map(int, input().split())) for _ in range(h)]
bl=[ list(map(int, input().split())) for _ in range(h)]

MAX=6500
dp=[[False]*MAX for _ in range(h*w)]
dp[0][abs(al[0][0]-bl[0][0])]=True

for y in range(h):
    for x in range(w):
        ind=pos(y,x)
        ind1=pos(y+1,x)
        ind2=pos(y,x+1)
        if y!=h-1: val1=abs(al[y+1][x]-bl[y+1][x])
        if x!=w-1: val2=abs(al[y][x+1]-bl[y][x+1])
        for j in range(MAX):
            if y!=h-1:
                if not dp[ind][j]:continue
                if j+val1<MAX: dp[ind1][j+val1]=True
                dp[ind1][abs(j-val1)]=True

            if x!=w-1:
                if not dp[ind][j]:continue
                if j+val2<MAX: dp[ind2][j+val2]=True
                dp[ind2][abs(j-val2)]=True

for i in range(MAX):
    if dp[h*w-1][i]:
        print(i)
        exit()