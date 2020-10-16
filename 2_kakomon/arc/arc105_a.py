al = list(map(int, input().split()))
al.sort()

if al[0]+al[1]+al[2] == al[3]:
    print('Yes')
elif al[0]+al[2] == al[3]+al[1]:
    print('Yes')
elif al[0]+al[2] == al[3]+al[1]:
    print('Yes')
elif al[1]+al[2] == al[0]+al[3]:
    print('Yes')
else:
    print('No')