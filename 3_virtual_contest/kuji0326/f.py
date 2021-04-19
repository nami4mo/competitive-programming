n=int(input())
d1,d2,d3,d4=[],[],[],[]
for _ in range(n):
    s=input()
    worst=0
    best=0
    lc=0
    for si in s:
        if si=='(':lc+=1
        else: lc-=1
        worst=min(worst,lc)
        best=max(best,lc)
    if worst>=0 and lc>=0: d1.append((lc,worst,0))
    elif worst< 0 and lc>=0: d2.append((lc,worst,0))

    else:
        best=0
        # worst=0
        lc=0
        for si in s[::-1]:
            if si=='(':lc+=1
            else: lc-=1
            # worst=min(worst,lc)
            best=max(best,lc)
        if best>0 and lc<0: d3.append((lc,worst,best))
        elif best<=0 and lc<0: d4.append((lc,worst,best))


d2.sort(reverse=True, key=lambda x:x[1])
d3.sort(reverse=True, key=lambda x:x[2])

# print(d1,d2,d3,d4)
# print(d1)
# print(d2)
# print(d3)
# print(d4)
lc=0
for c,worst,_ in d1+d2+d3+d4:
    if lc+worst<0:
        print('No')
        exit()
    else:
        lc+=c
    # print(lc)

if lc==0:
    print('Yes')
else:
    print('No')