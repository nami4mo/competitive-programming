n,a,b,c=map(int, input().split())
sl=[input() for _ in range(n)]

ansl = []
for i in range(n):
    si = sl[i]
    next_si = sl[i+1] if i < n-1 else '' 
    if si == 'AB':
        if a == 0:
            a+=1
            ansl.append('A')
            b-=1
        elif b == 0:
            a-=1
            b+=1
            ansl.append('B')
        else:
            if next_si == 'AC':
                b-=1
                a+=1
                ansl.append('A')
            elif next_si == 'BC':
                b+=1
                ansl.append('B')
                a-=1
            else:
                a-=1
                b+=1
                ansl.append('B')

    if si == 'AC':
        if a == 0:
            a+=1
            ansl.append('A')
            c-=1
        elif c == 0:
            a-=1
            c+=1
            ansl.append('C')
        else:
            if next_si == 'AB':
                c-=1
                a+=1
                ansl.append('A')
            elif next_si == 'BC':
                c+=1
                ansl.append('C')
                a-=1
            else:
                a-=1
                c+=1
                ansl.append('C')

    if si == 'BC':
        if b == 0:
            b+=1
            ansl.append('B')
            c-=1
        elif c == 0:
            b-=1
            c+=1
            ansl.append('C')
        else:
            if next_si == 'AB':
                c-=1
                b+=1
                ansl.append('B')
            elif next_si == 'AC':
                c+=1
                ansl.append('C')
                b-=1
            else:
                b-=1
                c+=1
                ansl.append('C')
    if a<0 or b<0 or c<0:
        print('No')
        exit()

print('Yes')
for a in ansl:print(a)