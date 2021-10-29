n=int(input())
keta=len(str(n))

if n<10:
    print(1)
    exit()

ans=0
for k in range(1,keta):
    for i in range(1,k):
        ans+=i*9*pow(10,k-i-1)
    ans+=k


sn=str(n)
if sn[0]>'1':
    for i in range(1,keta):
        ans+=i*9*pow(10,keta-i-1)
    ans+=keta
else:
    ok=False
    sn=str(n)
    for i in range(1,keta):
        # print(ans)
        if ok:
            ans+=i*9*pow(10,keta-i-1)
        else:
            rem_k=keta-i-1
            if sn[i]=='0':
                if rem_k!=0:
                    ans+=i*(int(sn[i+1:])+1)
                else:
                    ans+=i
                break
            elif sn[i]=='1':
                if rem_k!=0:
                    ans+=i*pow(10,rem_k)
                else:
                    ans+=i
            else:
                if rem_k!=0:
                    ans+=i*(int(sn[i:])+1)
                    ans-=i*pow(10,rem_k)
                else:
                    ans+=int(sn[i])
                ok=True
    else:
        # print(ans)
        ans+=keta
print(ans)