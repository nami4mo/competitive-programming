def check(bl):
    for i in range(19):
        for j in range(15):
            co,cx=0,0
            for k in range(5):
                if bl[i][j+k]=='o':co+=1
                if bl[i][j+k]=='x':cx+=1
            if co==5 or cx==5: return False
    for j in range(19):
        for i in range(15):
            co,cx=0,0
            for k in range(5):
                if bl[i+k][j]=='o':co+=1
                if bl[i+k][j]=='x':cx+=1
            if co==5 or cx==5: return False
    for i in range(15):
        for j in range(15):
            co,cx=0,0
            for k in range(5):
                if bl[i+k][j+k]=='o':co+=1
                if bl[i+k][j+k]=='x':cx+=1
            if co==5 or cx==5: return False

    for i in range(15):
        for j in range(4,19):
            co,cx=0,0
            for k in range(5):
                if bl[i+k][j-k]=='o':co+=1
                if bl[i+k][j-k]=='x':cx+=1
            if co==5 or cx==5: return False
    return True

bl=[list(input()) for _ in range(19)]
co,cx=0,0
for row in bl:
    co+=row.count('o')
    cx+=row.count('x')

if co==0 and cx==0:
    print('YES')
    exit()
# print(co,cx)
if co-1==cx:
    for i in range(19):
        for j in range(19):
            if bl[i][j]!='o':continue
            bl[i][j]='.'
            res=check(bl)
            if res:
                print('YES')
                exit()
            bl[i][j]='o'
    print('NO')
elif co==cx:
    for i in range(19):
        for j in range(19):
            if bl[i][j]!='x':continue
            bl[i][j]='.'
            res=check(bl)
            if res:
                print('YES')
                exit()
            bl[i][j]='x'
    print('NO')
else:
    print('NO')