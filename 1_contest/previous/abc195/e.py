n=int(input())
s=input()
x=input()

if n==1:
    if x[0]=='T':
        print('Takahashi')
    else:
        if int(s[0])%7==0:
            print('Takahashi')
        else:
            print('Aoki')
    exit()


dp=[False]*7
dp[0]=True
s1=int(s[-1])

for i in range(n-1,-1,-1):
    xi=x[i]
    si=int(s[i])
    new_dp=[False]*7
    if xi=='T':
        for m in range(7):
            if not dp[m]:continue
            for r in range(7):
                rem=(r*10+si)%7
                if rem==m:
                    new_dp[r]=True
                rem2=(r*10)%7
                if rem2==m:
                    new_dp[r]=True
    else:
        for r in range(7):
            rem=(r*10+si)%7
            rem2=(r*10)%7
            for m in range(7):
                if dp[rem] and dp[rem2]:
                    new_dp[r]=True
                
    dp=new_dp[:]

if dp[0]:
    print('Takahashi')
else:
    print('Aoki')