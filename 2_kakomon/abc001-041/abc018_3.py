r,c,k=map(int, input().split())
sl=[]
for _ in range(r):
    row=list(input())
    sl.append(row)


xsums=[]
for y in range(r):
    csums=[0]
    cs=0
    for si in sl[y]:
        if si=='x':cs+=1
        csums.append(cs)
    xsums.append(csums)

# print(xsums) 
k-=1 # mistake...
ans=0
for y in range(k,r-k):
    for x in range(k,c-k):
        # print('----',y,x)
        ok=True
        for i in range(0,k+1):
            yi1=y+i
            yi2=y-i
            
            l=x-(k-i)
            r=x+(k-i)
            cnt1=xsums[yi1][r+1]-xsums[yi1][l]
            cnt2=xsums[yi2][r+1]-xsums[yi2][l]
            if cnt1>0 or cnt2>0: ok=False

            # for xi in range(x-(k-i),x+(k-i)+1):
            #     if sl[yi1][xi]=='x':
            #         ok=False
            #     if sl[yi2][xi]=='x':
            #         ok=False
        # for xi in range(x-k,x+k+1):
        #     if sl[y][xi]=='x':ok=False
        if ok:ans+=1

print(ans)