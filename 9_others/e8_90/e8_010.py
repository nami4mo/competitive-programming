import sys
input = sys.stdin.readline

n=int(input())
c1=[0]
c2=[0]

for i in range(n):
    c,p=map(int, input().split())
    if c==1:
        c1.append(c1[-1]+p)
        c2.append(c2[-1])
    else:
        c1.append(c1[-1])
        c2.append(c2[-1]+p)

for _ in range(int(input())):
    l,r=map(int, input().split())
    a1=c1[r]-c1[l-1]
    a2=c2[r]-c2[l-1]
    print(a1,a2)