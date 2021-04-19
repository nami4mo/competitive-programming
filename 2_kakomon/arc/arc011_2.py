
d={}
dd=[('z','r'),('b','c'),('d','w'),('t','j'),('f','q'),('l','v'),('s','x'),('p','m'),('h','k'),('n','g')]
for num in range(10):
    a,b=dd[num]
    d[a]=str(num)
    d[b]=str(num)

tos=ord('a')-ord('A')

n=int(input())
wl=list(map(str, input().split()))
ans=[]
for w in wl:
    v=''
    for wi in w:
        if wi in d: v+=d[wi]
        if chr(ord(wi)+tos) in d: v+=d[chr(ord(wi)+tos)]

    if v: ans.append(v)
ans=' '.join(ans)
print(ans)