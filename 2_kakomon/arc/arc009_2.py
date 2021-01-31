bl=list(map(int, input().split()))
b2i=[0]*10
for i in range(10):
    b2i[bl[i]]=i


n=int(input())
ansl=[]
for j in range(n):
    orig_s=input()
    s=orig_s
    for i in range(10):
        s=s.replace(str(i),chr(b2i[i]+ord('a')))
    for i in range(10):
        s=s.replace(chr(i+ord('a')),str(i))
    # print(s)
    ansl.append((int(s),int(orig_s)))

ansl.sort()
for _,a in ansl:print(a)