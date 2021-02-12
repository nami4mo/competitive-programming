v,t,s,d=map(int, input().split())
a=t*v
b=s*v
if a<=d<=b:
    print('No')
else:
    print('Yes')