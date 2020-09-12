s = str(input())
q = int(input())

front_s = ''
back_s = ''
rev_flg = False

for i in range(q):
    query = list(map(str, input().split())) 
    if query[0] == '1':
        rev_flg = not rev_flg
    else:
        if not rev_flg:
            if query[1] == '1':
                front_s += query[2]
            else:
                back_s += query[2]
        else:
            if query[1] == '1':
                back_s += query[2]
            else:
                front_s += query[2]
    
res = front_s[::-1] + s + back_s
if rev_flg: res = res[::-1]
print(res) 