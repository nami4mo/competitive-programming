from collections import Counter
n=int(input())
dl=list(map(int, input().split()))
m=int(input())
tl=list(map(int, input().split()))
cd=Counter(dl)
ct=Counter(tl)
for diff,cnt in ct.items():
    if cd[diff]<cnt:
        print('NO')
        break
else:
    print('YES')