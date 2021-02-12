def update(dp,a):
    ca=a
    for v in dp:
        if v&(-v)&ca:ca^=v
    if ca==0: return 
    for i in range(len(dp)):
        if ca&(-ca)&dp[i]:dp[i]^=ca
    dp.append(ca)

def check(dp,a):
    ca=0
    for v in dp:
        if v&(-v)&a:ca^=v
    return ca==a

ansl=[]
for _ in range(int(input())):
    n=int(input())
    al=list(map(int, input().split()))
    s=input()
    dp=[0]
    for i in range(n-1,-1,-1):
        # print(dp)
        a=al[i]
        if s[i]=='0':
            update(dp,a)
        else:
            if not check(dp,a):
                ansl.append(1)
                break
    else:
        ansl.append(0)

for a in ansl:print(a)