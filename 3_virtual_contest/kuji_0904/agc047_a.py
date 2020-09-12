n = int(input())
al = []
for _ in range(n):
    s = input()
    if not '.' in s:
        al.append(int(s)*(10**9))
    else:
        syosu_keta = len(s.split('.')[1])
        rem = 9 - syosu_keta
        a = int(s.replace('.',''))
        a *= (10**rem)
        al.append(a)


al25 = [ [0]*19 for _ in range(19) ]
ans = 0
for a in al:
    cnt2 = 0
    cnt5 = 0
    curr_a = a
    for i in range(18):
        if curr_a%2 == 0:
            cnt2 += 1
            curr_a = curr_a//2
        else:
            break
    curr_a = a
    for i in range(18):
        if curr_a%5 == 0:
            cnt5 += 1
            curr_a = curr_a//5
        else:
            break

    for i in range(18-cnt2,19):
        for j in range(18-cnt5,19):
            ans += al25[i][j]

    al25[cnt2][cnt5] += 1

print(ans)