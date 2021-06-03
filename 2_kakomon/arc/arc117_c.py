n=int(input())
cl=input().replace('B','0').replace('W','1').replace('R','2')

frac=[1]*(n+10)
cnts3=[0]*(n+10)
fval=1
for i in range(1,n+10):
    val=i
    c3=0
    while val%3==0:
        val//=3
        c3+=1 
    fval=(fval*val)%3
    frac[i]=fval
    cnts3[i]=cnts3[i-1]+c3

ans=0
for i,c in enumerate(cl):
    v=int(c)
    if cnts3[n-1]>cnts3[n-i-1]+cnts3[i]:
        continue
    comb=frac[n-1]*frac[n-i-1]*frac[i]
    comb%=3
    # print(v,comb, frac[n-1], frac[n-i], frac[i])
    ans+=comb*v

ans%=3
if ans==0:print('B')
elif (ans==1 and n%2==1) or (ans==2 and n%2==0):print('W')
else:print('R')