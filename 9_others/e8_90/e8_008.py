n=int(input())
s=input()

ss='atcoder'
prev={}
for i in range(len(ss)-1):
    prev[ss[i+1]]=ss[i]

MOD=10**9+7
d={c:0 for c in ss}
for si in s:
    if si not in ss:continue
    if si=='a':d[si]+=1
    else:
        d[si]+=d[prev[si]]
        d[si]%=MOD
print(d['r'])