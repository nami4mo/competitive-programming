from bisect import bisect_left, bisect_right

s=input()
sn=len(s)
t=input()
tn=len(t)
alps = 'abcdefghijklmnopqrstuvwxyz' # string.ascii_lowercase
d={c:[] for c in alps}

for i in range(sn):
    si=s[i]
    d[si].append(i)

loop=0
pos=-1
for ti in t:
    if not d[ti]:
        print(-1)
        exit()
    ind = bisect_right(d[ti], pos)
    if not 0<=ind<len(d[ti]):
        loop+=1
        pos=d[ti][0]
    else:
        pos=d[ti][ind]

ans=loop*sn+pos+1
print(ans)    