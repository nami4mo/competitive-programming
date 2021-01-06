n=int(input())
yesl=[]
nol=[]
dd={}
for i in range(n):
    s=input()
    if s[0]=='!':
        dd.setdefault(s[1:],[False,False])
        dd[s[1:]][0]=True
    else:
        dd.setdefault(s,[False,False])
        dd[s][1]=True

for k,v in dd.items():
    if v[0] and v[1]:
        print(k)
        exit()
else:
    print('satisfiable')

