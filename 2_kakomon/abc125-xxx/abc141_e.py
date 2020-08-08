from collections import deque

n = int(input())
S = input()

for s, i in enumerate(S):
    same_s_inds = []
    for ii in range(i+1,n):
        if s[ii] == s:
            same_s_inds.append(ii)
    