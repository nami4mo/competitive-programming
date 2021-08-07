import sys
sys.setrecursionlimit(10**6)

n,q=map(int, input().split())
al=list(map(int, input().split()))
ql=[[True]*n for _ in range(n)]
for _ in range(q):
    x,y=map(int, input().split())
    x-=1
    y-=1
    ql[x][y]=False
    ql[y][x]=False

cl=[]
dic={}
def dfs(i, csum):
    # print(i,cl,csum)
    if i>=n: return
    # use
    for c in cl:
        if not ql[c][i]:break
    else:
        cl.append(i)
        val=csum+al[i]
        if val in dic:
            ans1=[a+1 for a in dic[val]]
            ans2=[a+1 for a in cl]
            print(len(ans1))
            print(*ans1)
            print(len(ans2))
            print(*ans2)
            exit()
        dic[val]=cl[:]
        dfs(i+1, csum+al[i])
        # end
        cl.pop()    
    # no use
    dfs(i+1, csum)

dfs(0,0)