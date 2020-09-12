s = input()
cf = False
for si in s:
    if si =='C': cf = True
    if cf and si == 'F':
        print('Yes')
        break
else:
    print('No')