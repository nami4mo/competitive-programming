ansl = []
for _ in range(int(input())):
    n,x =map(int, input().split())
    al = list(map(int, input().split()))
    
    al.sort()
    if al[0]==x and al[-1]==x:
        ansl.append(0)
        continue

    if x*n == sum(al):
        ansl.append(1)
    elif x in al:
        ansl.append(1)
    else:
        ansl.append(2)

for a in ansl: print(a)