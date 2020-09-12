n,x = map(int, input().split())
ll = list(map(int, input().split()))
cnt = 1
v = 0
for l in ll:
    v += l
    if v > x:
        break
    else:
        cnt += 1

print(cnt)