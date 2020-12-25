'''
    check ans candidates
'''
# from itertools import product
# n = 7
# bit = 7
# ite = list(product(range(bit),repeat=n))
# ans_st = set()
# for pattern in ite:
#     pattern = list(pattern)
#     al = []
#     for i in range(n):
#         st = set()
#         for j in range(n):
#             if j==i: continue
#             st.add(pattern[j])
#         al.append(len(st))
#     al.sort()
#     ans_st.add(tuple(al))

# # print(**ans_st)
# ansl = list(ans_st)
# ansl.sort()
# for a in ansl: print(a)

'''
(1, 1, 1, 1, 1, 1, 1)
(1, 2, 2, 2, 2, 2, 2)
(2, 2, 2, 2, 2, 2, 2)
(2, 2, 3, 3, 3, 3, 3)
(2, 3, 3, 3, 3, 3, 3)
(3, 3, 3, 3, 3, 3, 3)
(3, 3, 3, 4, 4, 4, 4)
(3, 3, 4, 4, 4, 4, 4)
(3, 4, 4, 4, 4, 4, 4)
(4, 4, 4, 4, 5, 5, 5)
(4, 4, 4, 5, 5, 5, 5)
(5, 5, 5, 5, 5, 6, 6)
(6, 6, 6, 6, 6, 6, 6)
'''

n=int(input())
al=list(map(int, input().split()))
al.sort()
if al[-1]-al[0]>1:
    print('No')
    exit()

# if n==2:
#     if al[0]==1 and al[1]==1:
#         print('Yes')
#     else:
#         print('No')
#     exit()

if al[-1]==al[0]:
    if al[0] <= n//2:
        print('Yes')
        exit()

if al[-1]==n-1 and al[0]==n-1:
    print('Yes')
    exit()

small = al[0]
small_cnt = al.count(small)
large_cnt = n-small_cnt

large_pair_max = large_cnt//2
if small_cnt <= small <= small_cnt+large_pair_max-1:
    print('Yes')
else:
    print('No')