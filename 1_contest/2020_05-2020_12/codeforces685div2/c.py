import sys
input = sys.stdin.readline

ansl = []
for _ in range(int(input())):
    n,k = map(int, input().split())
    sa = input().rstrip()
    sb = input().rstrip()
    alp_da = {chr(ord('a') + i): 0 for i in range(27)}
    alp_db = {chr(ord('a') + i): 0 for i in range(27)}
    
    for si in sa: alp_da[si] += 1
    for si in sb: alp_db[si] += 1

    alps = 'abcdefghijklmnopqrstuvwxyzA'
    for i in range(26):
        calp = alps[i]
        nalp = alps[i+1]
        if alp_da[calp] > alp_db[calp]:
            diff = alp_da[calp]-alp_db[calp]
            if diff%k == 0:
                alp_da[nalp] += diff
        elif alp_da[calp] < alp_db[calp]:
            ansl.append('No')
            break
    else:
        ansl.append('Yes')

for a in ansl:print(a)