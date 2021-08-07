ansl=[]
INF=10**10
for _ in range(int(input())):
    x,y,s=map(str, input().split())
    x,y=int(x),int(y)
    dp_c=INF
    dp_j=INF
    if s[0]=='C': dp_c=0
    if s[0]=='J': dp_j=0
    if s[0]=='?': dp_c,dp_j=0,0

    for si in s[1:]:
        if si=='C':
            dp_j,dp_c = INF, min(dp_c, dp_j+y)
        elif si=='J':
            dp_c, dp_j = INF, min(dp_j, dp_c+x)
        else:
            dp_c, dp_j = min(dp_c, dp_j+y), min(dp_j, dp_c+x)
    ans=min(dp_c,dp_j)
    ansl.append(ans)

for i,a in enumerate(ansl):
    print(f'Case #{i+1}: {a}')
    # print('Case {}: {}'.format(i,a))