# def soinsu(n):
#     curr_n = n
#     soinsu_d = {}
#     for i in range(2, n+1):
#         if i**2 > n: break
#         if n%i == 0:
#             while curr_n%i == 0:
#                 soinsu_d.setdefault(i,0)
#                 soinsu_d[i] += 1
#                 curr_n /= i
#     return soinsu_d

# def lcm(n, m):
#     n_s = soinsu(n)
#     m_s = soinsu(m)
#     n_sosu = n_s.keys()
#     m_sosu = m_s.keys()
#     sosu_all = list(set(n_sosu) | set(m_sosu))
#     curr_lcm = 1
#     for sosu in sosu_all:
#         sosu_a = n_s[sosu] if sosu in 


# import math
import fractions

a, b = map(int, input().split()) 
print(a*b//fractions.gcd(a,b))