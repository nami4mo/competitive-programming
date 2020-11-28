n,k=map(int, input().split())
s=input()
s=list(s)

curr_l = s[:] + s[:]
for i in range(k):
    new_l = []
    for j in range(n):
        a = curr_l[j*2]
        b = curr_l[j*2+1]
        if a =='R' and b=='S':
            new_l.append('R')
        elif a=='S' and b=='P':
            new_l.append('S')
        elif a=='P' and b=='R':
            new_l.append('P')
        elif b=='R' and a=='S':
            new_l.append('R')
        elif b=='S' and a=='P':
            new_l.append('S')
        elif b=='P' and a=='R':
            new_l.append('P')
        else:
            new_l.append(a)
    curr_l = new_l[:] + new_l[:]

print(curr_l[0])