n = int(input())
ll = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a,b,c = ll[i], ll[j], ll[k]
            if a == b or b == c or c == a:
                continue
            vs = [a,b,c]
            vs.sort()
            if vs[0] + vs[1] > vs[2]: 
                cnt += 1
                # print(vs)

print(cnt)
