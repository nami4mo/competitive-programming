# n = int(input())

# # 1行 1-str
# s_list = []
# for i in range(n):
#     s = str(input())
#     s_list.append(s)

# s_list = list(set(s_list))
# print(len(s_list))



# list_2019s = [i*2019 for i in range(1000)]
# print(list_2019s)
# import re

# s = str(input())
# list_2019s = ["12114", "14133", "16152"]
# cnt = 0
# for num in list_2019s:   
#     # cnt += s.count(num)
#     cnt += len(re.findall(num, s))

# # if 
# # 18171

# list_1817 = [m.span() for m in re.finditer('1817', s)]
# for num in list_1817:
#     if s[num[-1]] == '1': cnt+= 1

# print(cnt)


# import math
# from functools import reduce
# # def gcd(*numbers):
# #     return reduce(math.gcd, numbers)

# k = int(input())
# res = 0
# for c in range(1,k+1):
#     for b in range(1,k+1):
#         gcd_cd = math.gcd(c,b)
#         for a in range(1,k+1):
#             # res += gcd(a,b,c)
#             gcd_abc = math.gcd(a,gcd_cd)
#             res += gcd_abc
# print(res)

# n = int(input())
# s = str(input())

# r = s.count('R')
# g = s.count('G')
# b = s.count('B')
# all_count = r*g*b

# reduce = 0
# for i in range(1, n-2+1):
#     for j in range(i+1, (n+i)//2+1):
#         k = 2*j -i
#         if k > n: continue
#         if s[i-1] != s[j-1] and s[i-1] != s[k-1] and s[j-1] != s[k-1]:
#             reduce += 1
# print(all_count - reduce)

# a, b , c = map(int, input().split()) 
# a, b = b, a
# a,c = c, a
# print(a,b,c)

# n, m = map(int, input().split()) 
# a_list = list(map(int, input().split())) 
# a_sum = sum(a_list)

# cnt = 0
# for a in a_list:
#     if a >= a_sum / (4*m): cnt += 1

# if cnt >= m: print('Yes')
# else: print('No')

n, k = map(int, input().split()) 
rem = n%k
rem_minus_abs = abs(rem - k)
print(min(rem,rem_minus_abs))