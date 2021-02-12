s,p = map(int, input().split())
for n in range(1,10**6+1):
    m = s-n
    if m < 0: continue
    if m*n == p: 
        print('Yes')
        exit()
print('No')