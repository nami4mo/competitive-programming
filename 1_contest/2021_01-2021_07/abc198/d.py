from itertools import permutations

s1,s2,s3=(input()),(input()),(input())
n1,n2,n3=len(s1),len(s2),len(s3)

st=set()
for si in s1+s2+s3: st.add(si)

if len(st)>10:
    print('UNSOLVABLE')
    exit()

ll = list(st)
while len(ll)<10: ll.append('.')

for i in range(10):
    c=str(i)
    s1=s1.replace(ll[i],c)
    s2=s2.replace(ll[i],c)
    s3=s3.replace(ll[i],c)

s1,s2,s3=list(s1),list(s2),list(s3)
s1=[int(v) for v in s1]
s2=[int(v) for v in s2]
s3=[int(v) for v in s3]

r1=s1[::-1]
r2=s2[::-1]
r3=s3[::-1]

perml = list(permutations(list(range(10)), 10))
for perm in perml:
    perm=list(perm)
    # ctoi={}
    ctoi=[-1]*10
    for i in range(10):
        ctoi[perm[i]]=i
    ss1,ss2,ss3=0,0,0
    ok=True
    ten=1
    if ctoi[s1[0]]==0 or ctoi[s2[0]]==0 or ctoi[s3[0]]==0:continue
    for si in r1:
        ss1+=ten*ctoi[si]
        ten*=10
    ten=1
    for si in r2:
        ss2+=ten*ctoi[si]
        ten*=10
    ten=1
    for si in r3:
        ss3+=ten*ctoi[si]
        ten*=10
    if ss1+ss2==ss3:
        print(ss1)
        print(ss2)
        print(ss3)
        exit()
print('UNSOLVABLE')

