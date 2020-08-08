# https://atcoder.jp/contests/abc079/tasks/abc079_c

s = str(input())
nl = [s[0],s[1],s[2],s[3]]
nl = list(map(int,nl))

dic = {'+':1, '-':-1}
end = False
for op1 in ['+','-']:
    for op2 in ['+','-']:
        for op3 in ['+','-']:
            num = nl[0] + nl[1]*dic[op1] + nl[2]*dic[op2] + nl[3]*dic[op3]
            if num == 7 and not end:
                print('{}{}{}{}{}{}{}=7'.format(s[0],op1,s[1],op2,s[2],op3,s[3]))
                end = True