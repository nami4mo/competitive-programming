from random import randint, shuffle, sample, choice
from copy import deepcopy

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



def solve_main(n,k,pl,cl):
    pl = [0] + pl
    cl = [0] + cl
    ans = (10**18)*(-1)
    for start in range(1,n+1):
        val = 0
        vals = []
        already_set = set()
        curr_mass = start
        while True:
            next_mass = pl[curr_mass]
            point = cl[next_mass]
            if next_mass in already_set:
                break
            else:
                vals.append(point)
                already_set.add(next_mass)
                curr_mass = next_mass
        # print(vals)
        if k <= len(vals):
            c_max = vals[0]
            c_val = vals[0]
            # if len(vals) > 1:
            for v in vals[1:k]:
                c_val += v
                c_max = max(c_max, c_val)
            # print(c_max)
            ans = max(c_max,ans)
        else:
            v_sum = sum(vals)
            if v_sum <= 0:
                c_max = vals[0]
                c_val = vals[0]
                # if len(vals) > 1:
                for v in vals[1:]:
                    c_val += v
                    c_max = max(c_max, c_val)
                # print(c_max)
                ans = max(c_max,ans)
            else:
                if k%len(vals) > 0:
                    loop_cnt = k//len(vals)
                    rem = k - loop_cnt*len(vals)
                    c_max = v_sum*loop_cnt
                    c_val = v_sum*loop_cnt
                    if rem > 0:
                        for v in vals[:rem]:
                            c_val += v
                            c_max = max(c_max, c_val)
                    # print(c_max)
                    ans = max(c_max,ans)
                else:
                    loop_cnt = k//len(vals) - 1
                    rem = len(vals)
                    c_max = v_sum*loop_cnt
                    c_val = v_sum*loop_cnt
                    if rem > 0:
                        for v in vals[:rem]:
                            c_val += v
                            c_max = max(c_max, c_val)
                    # print(c_max)
                    ans = max(c_max,ans)
    return ans


def solve_comp(n,k,pl,cl):
    pl = [0] + pl
    cl = [0] + cl
    ans = -1*(10**9)
    for start in range(1,n+1):
        pos = start
        next_pos = pl[pos]
        curr_max = cl[next_pos]
        val = 0
        for i in range(k):
            next_pos = pl[pos]
            val += cl[next_pos]
            curr_max = max(curr_max, val)
            pos = next_pos
        ans = max(curr_max, ans)
    return ans


if __name__ == "__main__":
    LOOP_CNT = 100
    wa_cnt = 0
    for _ in range(LOOP_CNT):
        # generate test cases here
        n = randi(2,7)
        k = randi(1,10)
        cl = randil(-10,10,n)
        while True:
            pl = randil_unique(1,n,n)
            for i in range(n):
                if i+1 == pl[i]:
                    continue
            else:
                break
        ans_main = solve_main(n,k,pl[:],cl[:])
        ans_comp = solve_comp(n,k,pl[:],cl[:])
        if ans_main != ans_comp:
            print('--------')
            # print test case values here
            print(n,k)
            print(*pl)
            print(*cl)
            print(f'main: {ans_main}')
            print(f'comp: {ans_comp}')
            wa_cnt += 1
    print('=======')
    print(f'WA count: {wa_cnt}/{LOOP_CNT}')