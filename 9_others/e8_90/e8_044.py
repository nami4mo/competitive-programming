import sys
input = sys.stdin.readline

n,q=map(int, input().split())
al=list(map(int, input().split()))
move=0
for _ in range(q):
    t,x,y=map(int, input().split())
    x-=1
    y-=1
    x=(x-move)%n
    y=(y-move)%n
    if t==1:
        al[x],al[y]=al[y],al[x]
    elif t==2:
        move+=1
    else:
        print(al[x])
