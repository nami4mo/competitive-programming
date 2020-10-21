h,w,n = map(int, input().split())
r,c = map(int, input().split())
s = input()
t = input()

l = 1
ri = w
for i in range(n-1,-1,-1):
    if i != n-1:
        if t[i] == 'R':
            l-=1
            l = max(1,l)
        elif t[i] == 'L':
            ri+=1
            ri = min(ri,w)

    if s[i] == 'L':
        l += 1
    elif s[i] == 'R':
        ri-= 1

    if ri < l:
        print('NO')
        exit()


    
if not(l <= c <= ri):
    print('NO')
    exit()

# print('a')

l = 1
ri = h
for i in range(n-1,-1,-1):
    if i != n-1:
        if t[i] == 'D':
            l-=1
            l = max(1,l)
        elif t[i] == 'U':
            ri+=1
            ri = min(ri,h)

    if s[i] == 'U':
        l += 1
    elif s[i] == 'D':
        ri-= 1

    if ri < l:
        print('NO')
        exit()

if not(l <= r <= ri):
    print('NO')
    exit()
    
print('YES')
