k=int(input())
s=input()
t=input()

rems=[k]*10
rems[0]=0

scnt=[0]*10
for si in s[:-1]:
    ssi=int(si)
    # print(ssi)
    scnt[ssi]+=1
    rems[ssi]-=1

tcnt=[0]*10
for ti in t[:-1]:
    tti=int(ti)
    tcnt[tti]+=1
    rems[tti]-=1

# print(scnt)
sv=0
for i in range(10):
    sv+=i*pow(10,scnt[i])

tv=0
for i in range(10):
    tv+=i*pow(10,tcnt[i])

# print(sv,tv)

all_rem=9*k-8
all_rem1=all_rem-1
ans=0
# print(rems)
for i in range(1,10):
    for j in range(1,10):
        scnt[i]+=1
        tcnt[j]+=1
        sv=0
        for k in range(10):
            sv+=k*pow(10,scnt[k])
        tv=0
        for k in range(10):
            tv+=k*pow(10,tcnt[k])
        scnt[i]-=1
        tcnt[j]-=1
        if sv<=tv:continue

        if i!=j:
            prob=(rems[i]/all_rem)*(rems[j]/all_rem1)
            # print(i,j,prob)
            ans+=prob
        else:
            prob=(rems[i]/all_rem)*((rems[j]-1)/all_rem1)
            ans+=prob
print(ans)
