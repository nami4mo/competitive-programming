def sign(a):
    return 1 if a>=0 else -1

def modify(xs,ys,swap,ansl):
    new_ansl=[]
    for x,y in ansl:
        cx,cy=x,y
        if swap:cx,cy=cy,cx
        cx*=xs
        cy*=ys
        new_ansl.append((cx,cy))
    return new_ansl

def solve():
    k=int(input())
    x,y=map(int, input().split())
    xs=sign(x)
    ys=sign(y)
    x,y=abs(x),abs(y)
    swap=False
    if y>x:
        x,y=y,x
        swap=True

    if (x+y)%k==0:
        ans=(x+y)//k
        ansl=[]
        cx,cy=0,0
        for i in range(ans):
            if cx+k<=x:
                ansl.append((cx+k,0))
                cx+=k
            elif cx<x and cx+k>x:
                ansl.append((x,k-(x-cx)))
                cy=k-(x-cx)
                cx=x

            else:
                cy+=k
                ansl.append((x,cy))
        return ans, modify(xs,ys,swap,ansl)

    need=k-(x+y)%k
    if need%2==1:
        if k%2==0:
            return -1,[]
        else:
            need+=k

    d=x+y+need
    cnt=d//k
    if cnt>=2:
        a=need//2
        ans=cnt
        ansl=[]
        di=0
        cx,cy=0,0
        for i in range(ans):
            if di==0:
                if cy-k>(-1)*a:
                    cy-=k
                    ansl.append((0,cy))
                else:
                    di=1
                    rem=(-1)*a-(cy-k)
                    cx=rem
                    ansl.append((cx,-a))
            elif di==1:
                if cx+k<x:
                    cx+=k
                    ansl.append((cx,-a))
                else:
                    di=2
                    rem=cx+k-x
                    cy=(-a)+rem
                    ansl.append((x,cy))
            else:
                cy+=k
                ansl.append((x,cy))
        return ans, modify(xs,ys,swap,ansl)

    atop=2*k-(x+y)
    if atop%2==0:
        a=atop//2
        b=(x+y)//2
        ansl=[(b,-a),(x,y)]
        return 2, modify(xs,ys,swap,ansl)



    # print(3)
    rem=(3*k-(x+y))
    ab=rem//2
    a=ab//2
    b=ab-a
    ans=3
    ansl=[(k-a,-a),(x+b,2*k-2*a-x-b),(x,y)]
    return ans,modify(xs,ys,swap,ansl)



ans,ansl=solve()
print(ans)
for a,b in ansl:print(a,b)