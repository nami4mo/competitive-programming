n, k = map(int, input().split())
r, s, p = map(int, input().split())
r, s, p = p, r, s
point = {'p':p, 'r':r, 's':s}

t = input()
lose_flag = []
ans = 0
for i in range(len(t)):
    if i >= k and t[i] == t[i-k] and not lose_flag[i-k]:
        lose_flag.append(True)
        continue
    lose_flag.append(False)
    ans += point[t[i]]
    # print(point[t[i]])
print(ans)