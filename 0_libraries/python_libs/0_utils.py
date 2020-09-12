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
dp = [ [ [0]*l  for _ in range(m) ] for _ in range(n) ]


'''
    [2-dim cumulative sum]
'''
al = [1,2,6,3,10]
csums = [ [0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        csums[i+1][j+1] = csums[i+1][j] + csums[i][j+1] - csums[i][j] + al[i][j]


'''
    [math.ceil]
'''
v = (a-1)//b + 1
v = (a+b-1)//b


'''
    [count continuous values]
    (e.g.) 1 1 2 3 3 2 -> [(1, 1), (2, 1), (3, 2), (2, 1)]
'''
al = list(map(int, input().split()))
cntl = []
prev = al[0]
cnt = 0
for a in al[1:]:
    if prev == a: cnt+=1
    else:
        cntl.append((prev,cnt))
        cnt = 1
        prev = a
cntl.append((prev,cnt))