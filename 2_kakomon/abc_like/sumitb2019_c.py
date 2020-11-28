x = int(input())
cnt100 = x//100
rem = x%100
if cnt100*5 >= rem:
    print('1')
else:
    print('0')