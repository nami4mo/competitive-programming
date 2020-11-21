import sys
input = sys.stdin.readline

n = int(input())

finded = [ [] for _ in range(n) ]
flag = False
base = -1
for i in range(2,n+1):
    print('XOR', 1, i, flush=True)
    x = int(input())
    if len(finded[x]) > 0 and not flag:
        a = finded[x][0] # ind
        b = i # ind
        print('OR', a, b, flush=True)
        abv = int(input())
        base = abv^x
        flag = True
    finded[x].append(i)


if base == -1:
    if finded[0] and finded[n-1]:
        a,b = finded[0][0], finded[n-1][0]
        print('OR', a, 1, flush=True)
        aa = int(input())
        print('OR', b, 1, flush=True)
        bb = int(input())
        base = aa&bb
    elif finded[1] and finded[n-2]:
        a,b = finded[1][0], finded[n-2][0]
        print('OR', a, 1, flush=True)
        aa = int(input())
        print('OR', b, 1, flush=True)
        bb = int(input())
        base = aa&bb
    else:
        a,b = finded[2][0], finded[n-3][0]
        print('OR', a, 1, flush=True)
        aa = int(input())
        print('OR', b, 1, flush=True)
        bb = int(input())
        base = aa&bb

ansl = [0]*n

for x in range(n):
    val = x^base
    for i in finded[x]:
        ansl[i-1] = val

ansl[0] = base
print('!',*ansl)

