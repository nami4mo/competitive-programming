n = int(input())
if n == 1:
    print('Yes')
    print(2)
    print(1,1)
    print(1,1)
    exit()


for i in range(2,10**3):
    if i*(i+1) == n*2:
        k,l = i+1, i
        break
else:
    print('No')
    exit()

print('Yes')

ans = [ [] for _ in range(k)]
top = 0
bottom = 1
for i in range(1,n+1):
    ans[top].append(i)
    ans[bottom].append(i)
    if bottom < k-1:
        bottom += 1
    else:
        top += 1
        bottom = top+1

print(len(ans))
for row in ans:
    print(len(row), *row )