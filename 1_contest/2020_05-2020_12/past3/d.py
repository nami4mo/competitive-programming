def l(v):
    return v == '#'
def lc(c,y,x):
    return c[y][x] == '#'

n = int(input())
sl = []
for _ in range(5):
    sl.append(list(input()))

ans = ''
for i in range(n):
    curr_i = i+1
    c = []
    for r in range(5):
        c.append( sl[r][4*curr_i-3:4*curr_i] )
    if l(c[0][1]) and l(c[4][1]) and not l(c[1][1]) and not l(c[2][1]) and not l(c[3][1]):
        ans += '0'
    elif l(c[0][1]) and l(c[1][1]) and  l(c[2][1]) and  l(c[3][1]) and  l(c[4][1]):
        ans += '1'
    elif l(c[0][0]) and not l(c[1][0]) and  l(c[2][0]) and  l(c[3][0]) and  l(c[4][0]):
        ans += '2'
    elif l(c[0][0]) and not l(c[1][0]) and  l(c[2][0]) and  not l(c[3][0]) and  l(c[4][0]):
        ans += '3'
    elif l(c[0][0]) and  l(c[1][0]) and  l(c[2][0]) and  not l(c[3][0]) and  not l(c[4][0]):
        ans += '4'
    elif l(c[0][0]) and not l(c[1][0]) and not l(c[2][0]) and  not l(c[3][0]) and  not l(c[4][0]):
        ans += '7'
    elif lc(c,0,0) and lc(c,1,0) and lc(c,2,0) and not lc(c,3,0):
        if not lc(c,1,2):
            ans += '5'
        else:
            ans += '9'
    elif lc(c,1,2):
        ans += '8'
    else:
        ans += '6'


print(ans)
