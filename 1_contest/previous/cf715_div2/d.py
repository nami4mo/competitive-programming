# import sys
# input = sys.stdin.readline
for _ in range(int(input())):
    sl=[]
    n=int(input())
    for _ in range(3):
        sl.append(input())
    al=[]
    for i in range(2*n):
        c0=0
        for j in range(3):
            if sl[j][i]=='0':c0+=1
        if c0>=2:
            al.append('0')
        else:
            al.append('1')
    for i in range(n):
        if al[n+i]=='0':al.append('1')
        else:al.append('0')
    print(''.join(al))