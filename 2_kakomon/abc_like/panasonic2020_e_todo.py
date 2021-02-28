def solve(a,b,c):
    for lshift in range(0,len(a)+1):
        ss=[]
        for i in range(len(b)):
            ai=i+lshift
            if 0<=ai<len(a):
                if a[ai]==b[i]:
                    if a[ai]=='?':ss.append('?')
                    else: ss.append(a[ai])
                else:
                    c1,c2=a[ai],b[i]
                    if c2=='?': c1,c2=c2,c1
                    if c1=='?': ss.append(c2)
                    else: break
        # else:
        #     for rshift in range(0,len(b)+1):
                


a=input()
b=input()
c=input()
