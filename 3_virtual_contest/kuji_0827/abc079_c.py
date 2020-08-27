s = list(input())
# v = list(map(int,s))

for a in ['+','-']:
    for b in ['+','-']:
        for c in ['+','-']:
            cal = s[0]+a+s[1]+b+s[2]+c+s[3]
            v = eval(cal)
            if v == 7:
                print(cal+'=7')
                exit()