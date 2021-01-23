import sys
sys.setrecursionlimit(10**6)

dp=[(-1,-1)]*(3**9)
bl=[]
cl=[]

def rec(state):
    if dp[state]!=(-1,-1):return dp[state]
    v9=[-1]*9
    end=True
    cnt=0
    emptyl=[]
    c_state=state
    for i in range(9):
        v9[i]=c_state%3
        if v9[i]==0:
            end=False
            emptyl.append(i)
        else: cnt+=1
        c_state//=3

    if end:
        boy=0
        girl=0
        for i in range(2):
            for j in range(3):
                if v9[i*3+j] == v9[(i+1)*3+j]:
                    boy+=bl[i][j]
                else:
                    girl+=bl[i][j]
        for i in range(3):
            for j in range(2):
                if v9[i*3+j] == v9[i*3+j+1]:
                    boy+=cl[i][j]
                else:
                    girl+=cl[i][j]
        dp[state]=(boy,girl)
        return (boy,girl)
    
    if cnt%2==0: # boy's turn
        boy_max, girl=0,0
        for empty in emptyl:
            c_boy,c_girl=rec(state+1*(3**empty))
            if c_boy>=boy_max:
                boy_max,girl=c_boy,c_girl
        dp[state]=(boy_max,girl)
        return (boy_max,girl)
    else:
        boy, girl_max=0,0
        for empty in emptyl:
            c_boy,c_girl=rec(state+2*(3**empty))
            if c_girl>=girl_max:
                boy, girl_max=c_boy,c_girl
        dp[state]=(boy,girl_max)
        return (boy,girl_max)


bl.append(list(map(int, input().split())))
bl.append(list(map(int, input().split())))
cl.append(list(map(int, input().split())))
cl.append(list(map(int, input().split())))
cl.append(list(map(int, input().split())))
b,g=rec(0)
print(b)
print(g)