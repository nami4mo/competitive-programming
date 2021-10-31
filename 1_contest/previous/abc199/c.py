s=['a','b']
s[0],s[1]=s[1],s[0]

n=int(input())
s=list(input())
q=int(input())

def num(a):
    if a<n:return a+n
    else: return a-n

flip=False
for _ in range(q):
    t,a,b=map(int, input().split())
    a-=1
    b-=1
    if t==2:
        flip= not flip
    else:
        if flip:
            a=num(a)
            b=num(b)
        s[a],s[b]=s[b],s[a]

if flip:
    ans=s[n:]+s[:n]
else:
    ans=s[:n]+s[n:]
print(''.join(ans))