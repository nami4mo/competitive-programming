n=int(input())
s=input()

jc=0
oc=0
cnt=0
for si in s+'I':
    if si=='J':jc+=1
    if si=='O':oc+=jc
    if si=='I':cnt+=oc

jc=0
oc=0
cnt2=0
for si in 'J'+s:
    if si=='J':jc+=1
    if si=='O':oc+=jc
    if si=='I':cnt2+=oc

jc=0
oc=0
ol=[]
cnt3=0
jl=[]
for si in s:
    if si=='J':jc+=1
    if si=='O':oc+=jc
    if si=='I':
        ol.append(oc)
        cnt3+=oc
    jl.append(jc)

il=[-1]*n
ic=0
for i in range(n-1,-1,-1):
    si=s[i]
    if si=='I':ic+=1
    il[i]=ic
# print(cnt3)
# print(jl)
# print(il)
cnt33=cnt3
for i in range(n):
    cnt33=max(cnt33,cnt3+jl[i]*il[i])

print(max(cnt,cnt2,cnt33))