class P:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def cross(a,b,c,d): # cross? AB CD
    s = (a.x - b.x) * (c.y - a.y) - (a.y - b.y) * (c.x - a.x)
    t = (a.x - b.x) * (d.y - a.y) - (a.y - b.y) * (d.x - a.x)
    if s*t>0: return False
    s = (c.x - d.x) * (a.y - c.y) - (c.y - d.y) * (a.x - c.x)
    t = (c.x - d.x) * (b.y - c.y) - (c.y - d.y) * (b.x - c.x)
    if s*t>0: return False
    return True

a,b,c,d=map(int, input().split())
pa=P(a,b)
pb=P(c,d)

ps=[]
n=int(input())
for _ in range(n):
    x,y=map(int, input().split())
    ps.append(P(x,y))

ps.append(ps[0])
cnt=0
for i in range(n):
    if cross(pa,pb,ps[i],ps[i+1]):cnt+=1
cnt//=2
print(cnt+1)