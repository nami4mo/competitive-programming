q=int(input())
top=[]
tn=0
bottom=[]
bn=0
for _ in range(q):
    t,x=map(int, input().split())
    if t==1:
        top.append(x)
        tn+=1
    elif t==2:
        bottom.append(x)
        bn+=1
    else:
        if tn>=x:
            print(top[-x])
        else:
            print(bottom[x-tn-1])
