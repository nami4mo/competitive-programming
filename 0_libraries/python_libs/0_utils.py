''' [input] '''
import sys
input = sys.stdin.readline
input().rstrip() # remove last '\n'


''' [for DFS] '''
import sys
sys.setrecursionlimit(10**6)


''' [binary search] '''
# ng, ok = 0, 10**9+1
ok, ng = 0, 10**9+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    # ...
    if res: ok = mid
    else: ng = mid
print(ok)


''' [alphabet] '''
alps = 'abcdefghijklmnopqrstuvwxyz' # string.ascii_lowercase
alps = [chr(ord('a')+i) for i in range(26)]
alp_d = {chr(ord('a') + i): 0 for i in range(26)}
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # string.ascii_uppercase
ALPs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

ALPS = alps.upper()
alps = ALPS.lower()


''' [3d-list] '''
dp = [ [ [0]*l  for _ in range(m) ] for _ in range(n) ]


''' [1-dim cumulative sum] '''
al = [1,2,6,3,10]
csums = [0]*(n+1)
for i,a in enumerate(al):
    csums[i+1] = csums[i]+a


''' [2-dim cumulative sum] '''
al = [[1,2,6],[3,10,3],[3,4,1],[1,3,4]]
csums = [ [0]*(w+1) for _ in range(h+1)]
for i in range(h):
    for j in range(w):
        csums[i+1][j+1] = csums[i+1][j] + csums[i][j+1] - csums[i][j] + al[i][j]


''' [math.ceil] '''
v = (a-1)//b + 1


'''　[Run Length Encoding]　'''
al = [1,1,5,3,3,3,3,3,4,4,1,2,2]
cntl = []
prev = al[0]
cnt = 1
for a in al[1:]:
    if prev == a: cnt+=1
    else:
        cntl.append((prev,cnt))
        cnt = 1
        prev = a
cntl.append((prev,cnt))



''' [線分の交差判定] '''
class P:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def cross(a,b,c,d): # cross? AB CD
    s = (a.x - b.x) * (c.y - a.y) - (a.y - b.y) * (c.x - a.x)
    t = (a.x - b.x) * (d.y - a.y) - (a.y - b.y) * (d.x - a.x)
    if s*t>0: return False
    s = (c.x - d.x) * (a.y - c.y) - (c.y - d.y) * (a.x - c.x)
    t = (c.x - d.x) * (b.y - c.y) - (c.y - d.y) * (b.x - c.x)
    if s*t>0: return False
    return True


''' [2d-list debug print] '''
from time import sleep
def print_overwrite(list2d, val_width=5, sleep_sec=1.0, header=None):
    val_str = f'{header}\n' if header else '' 
    for row in list2d: 
        row_str = ' '.join(map(lambda v: str(v).rjust(val_width),row))
        val_str += f'{row_str}\n'
    new_line_cnt = val_str.count('\n')
    val_str += f'\033[{new_line_cnt}A'
    print(val_str, end='')
    sleep(sleep_sec)


''' bit 部分集合 3**n '''
for i in range(1<<n):
    bits=(i-1)&i
    while bits>0:
        bits=(bits-1)&i
        if bits==0:break
        comp=bits^i