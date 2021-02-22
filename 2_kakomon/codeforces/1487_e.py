import sys
input = sys.stdin.readline

INF=10**12
def update(al0, al1, gl01):
    ail0=[ (al0[i],i) for i in range(len(al0))]
    ail0.sort(key=lambda x:x[0])
    res=[INF]*len(al1)
    rems=list(range(len(al1)))
    for a,i in ail0:
        new_rems=[]
        for i1 in rems:
            if i1 in gl01[i]:
                new_rems.append(i1)
            else:
                res[i1]=a+al1[i1]
        rems=new_rems[:]
    # print(res)
    # al1=res
    for i in range(len(al1)):
        al1[i]=res[i] 

nl=list(map(int, input().split()))
al0=list(map(int, input().split()))
al1=list(map(int, input().split()))
al2=list(map(int, input().split()))
al3=list(map(int, input().split()))

g01=[set() for _ in range(nl[0])]
g12=[set() for _ in range(nl[1])]
g23=[set() for _ in range(nl[2])]
for _ in range(int(input())):
    a,b=map(int, input().split())
    g01[a-1].add(b-1)
for _ in range(int(input())):
    a,b=map(int, input().split())
    g12[a-1].add(b-1)
for _ in range(int(input())):
    a,b=map(int, input().split())
    g23[a-1].add(b-1)

# print(al1)
update(al0,al1,g01)
# print(al1)
update(al1,al2,g12)
# print(al2)
update(al2,al3,g23)
# print(al3)

ans=min(al3)
if ans>=INF: ans=-1
print(ans)