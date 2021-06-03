s=input()
sn=len(s)
t=input()
tn=len(t)

sa=[0]*(sn+1)
# sb=[0]*(sn+1)
ta=[0]*(sn+1)
# tb=[0]*(sn+1)

a,b=0,0
for i in range(sn):
    if s[i]=='A':a+=1
    # else: b+=1
    sa[i+1]=a
    # sb[i+1]=b

a,b=0,0
for i in range(tn):
    if t[i]=='A':a+=1
    # else: b+=1
    ta[i+1]=a
    # tb[i+1]=b


for _ in range(int(input())):
    a,b,c,d=map(int, input().split())
    sacnt=sa[b]-sa[a-1]
    sbcnt=b-a+1-sacnt
    tacnt=ta[d]-ta[c-1]
    tbcnt=d-c+1-tacnt
    # print(sacnt,sbcnt)
    # print(tacnt,tbcnt)
    if (sacnt-sbcnt)%3 == (tacnt-tbcnt)%3:
        print('YES')
    else:
        print('NO')