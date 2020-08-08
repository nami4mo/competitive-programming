n = int(input())
s = list(input())

r = s.count('R')
g = s.count('G')
b = s.count('B')

all_comb = r*g*b

reduce_cnt = 0
for i in range(n):
    for k in range(i+2,n):
        if (i+k)%2 == 1: continue
        j = (i+k)//2
        if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]: reduce_cnt += 1

print(all_comb-reduce_cnt)