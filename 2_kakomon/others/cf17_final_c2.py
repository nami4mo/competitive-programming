n = int(input())
dl = list(map(int, input().split()))

if 0 in dl:
    print(0)
    exit()

dl.sort()
dl1 = [0,24]
dl2 = [0,24]
for i, d in enumerate(dl):
    if i%2 == 0:
        dl1.append(d)
        dl2.append(24-d)
    else:
        dl1.append(24-d)
        dl2.append(d)

dl1.sort()
dl2.sort()

min_1 = 24
for a,b in zip(dl1[1:],dl1[:-1]):
    diff = a-b
    min_1 = min(min_1,diff)

min_2 = 24
for a,b in zip(dl2[1:],dl2[:-1]):
    diff = a-b
    min_2 = min(min_2,diff)

ans = max(min_1,min_2)
print(ans)
