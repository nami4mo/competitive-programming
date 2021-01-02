n,k = map(int, input().split())
cntd = {}

for _ in range(n):
    s = input()
    if s not in cntd: cntd[s] = 0
    cntd[s] += 1

cntl = [(-1,-1)]
for k_,v in cntd.items():
    cntl.append((v,k_))

cntl.append((10000000000,1000000000))
cntl.sort(reverse=True)

# print(cntl)
if cntl[k][0] != cntl[k-1][0] and cntl[k][0] != cntl[k+1][0]:
    print(cntl[k][1])
else:
    print('AMBIGUOUS')