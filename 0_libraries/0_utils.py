'''
    [input]
'''
import sys
input = sys.stdin.readline
input().rstrip() # remove last '\n'

a, b = map(int, input().split()) 
al = list(map(int, input().split())) 


'''
    [alphabet]
'''
import string 
alps = string.ascii_lowercase
alps = 'abcdefghijklmnopqrstuvwxyz'
alps = [chr(ord('a')+i) for i in range(26)]
alp_d = {chr(ord('a') + i): 0 for i in range(26)}

ALPS = string.ascii_uppercase
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ALPS = alps.upper()
alps = ALPS.lower()

ALPs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


'''
    [binary search]
'''
# ng, ok = 0, 10**9+1
ok, ng = 0, 10**9+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    ok_flag = True
    # ...
    if ok_flag:
        ok = mid
    else:
    	ng = mid
print(ok)



'''
    [list]
'''
dp = [ [ [0]*L  for _ in range(M) ] for _ in range(N) ]