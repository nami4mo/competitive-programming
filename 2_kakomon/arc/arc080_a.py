n=int(input())
al=list(map(int, input().split()))
cnt0=0
cnt4=0
cnt2=0
for a in al:
    if a%2 != 0:cnt0+=1
    if a%4==0: cnt4+=1
    elif a%2==0:cnt2+=1

if cnt2 > 0:
    if cnt4 >= cnt0:print('Yes')
    else:print('No')
else:
    if cnt4+1 >= cnt0:print('Yes')
    else:print('No')