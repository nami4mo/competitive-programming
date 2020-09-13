from random import randint, shuffle, sample, choice
from copy import deepcopy
from itertools import permutations
from bisect import bisect_left, bisect_right

from collections import deque, Counter

# TODO: make "Tree test case" generator

# functions for making test cases
def randi(a,b): return randint(a,b)
def randil(a,b,n): return [ randint(a,b) for _ in range(n) ]  # list of N elements (a <= n <= b)
def randil_2d(a,b,h,w): return [ [randint(a,b) for _i in range(w)] for _j in range(h)]  # 2-dim list of HxW elements (a <= n <= b)
def randil_unique(a,b,n): return sample(list(range(a,b+1)), n)  # N-unique elements (a <= n <= b)

def rands(char_list, n): return ''.join([choice(char_list) for _ in range(n)]) # (e.g.) rands(['B','W'], 4) -> 'BBWB'
def randcl(char_list, n): return [choice(char_list) for _ in range(n)] # (e.g.) randsl(['B','W'], 4) -> ['B', 'B', 'W', 'B']
def rands_2d(char_list, h, w): return [''.join([choice(char_list) for _ in range(w)]) for _ in range(h)] # (e.g.) rands_2dim(['#','.'], 3,2) -> ['#.', '..', '.#']
def randcl_2d(char_list, h, w): return [[choice(char_list) for _ in range(w)] for _ in range(h)] # (e.g.) randsl_2dim(['#','.'], 3,2) -> [['.', '#'], ['#', '#'], ['.', '#']]

def rand_unique_points(n, x1, x2, y1, y2): return sample([(x,y) for x in range(x1,x2+1) for y in range(y1,y2+1)], n)  # N-unique XY points ( x1 <= x <= x2, y1 <= y <= y2 ) 



def solve_main(n,al,bl):
    # n = int(input())
    # al = list(map(int, input().split()))
    # bl = list(map(int, input().split()))

    c = Counter(al)
    cnt_mosts = c.most_common()
    avals = []
    for val,cnt in cnt_mosts:
        r = bisect_right(al, val) - 1
        l = bisect_left(al, val)
        avals.append((val,l,r))


    exist = [0]*(n+1)
    for a in al:
        exist[a] = True

    # bl.sort(reverse=True)

    bl.sort(reverse=True)
    c = Counter(bl)
    cnt_mosts = c.most_common()
    bl.sort()
    bvals = []
    for val,cnt in cnt_mosts:
        r = bisect_right(bl, val) - 1
        l = bisect_left(bl, val)
        bvals.append((val,r-l+1))
        # print(val, r-l+1)

    hayame = deque([])
    always = deque([])
    # for b in bl:
    for b, cnt in bvals:
        if exist[b]:
            for _ in range(cnt):
                hayame.append(b)
        else:
            for _ in range(cnt):
                always.append(b)



    ansl = [-1]*n
    # for a in al:
    for a, l, r in avals:
        for i in range(l,r+1):
            while hayame and hayame[0] == a:
                hayame.popleft()
                always.append(a)

            if hayame:
                poped = hayame.popleft()
                # ansl.append(poped)
                ansl[i] = poped
            elif always and always[0] != a:
                poped = always.popleft()
                # ansl.append(poped)
                ansl[i] = poped
            else:
                return ('No',[])

    return ('Yes', ansl)
    print('Yes')
    print(*ansl)

def solve_comp(n,al,bl):
    ll = list(range(1,n+1))  # list of elements
    perml = list(permutations(bl, n))
    for perm in perml:
        l = list(perm)
        for i in range(n):
            if al[i] == l[i]: break
        else:
            return ('Yes', l)
    else:
        return ('No', [])


if __name__ == "__main__":
    LOOP_CNT = 100
    wa_cnt = 0
    for _ in range(LOOP_CNT):
        n = 5
        al = randil(1,n,n)
        bl = randil(1,n,n)
        al.sort()
        bl.sort()
        ans_main = solve_main(n,al[:],bl[:])
        ans_comp = solve_comp(n,al[:],bl[:])
        if ans_main[0] != ans_comp[0]:
            print('--------')
            print(al)
            print(bl)
            # print test case values here
            print(f'main: {ans_main}')
            print(f'comp: {ans_comp}')
            wa_cnt += 1
    print('=======')
    print(f'WA count: {wa_cnt}/{LOOP_CNT}')