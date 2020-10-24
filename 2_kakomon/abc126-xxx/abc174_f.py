
# https://atcoder.jp/contests/abc140/tasks/abc140_e
# https://atcoder.jp/contests/agc005/tasks/agc005_b
# https://atcoder.jp/contests/abc157/tasks/abc157_e

''' 
    [Bit]
'''
import sys

class Bit:
    """ used for only int(>=0) 
        1-indexed (ignore 0-index)
    """
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


def main():
    input = sys.stdin.readline
    n,q = map(int, input().split())
    # cl = [0] + list(map(int, input().split()))
    cl = list(map(int, input().split()))
    posl = [-1]*(n+1)
    bit = Bit(n)
    ql = []
    for i in range(q):
        l,r = map(int, input().split())
        ql.append((i,l,r))
    ql.sort(key=lambda x: x[2])

    curr_r = 0
    ansl = [-1]*q
    for i,l,r in ql:
        while curr_r < r:
            curr_r+=1
            v = cl[curr_r-1]
            bit.add(curr_r,1)
            if posl[v] != -1:
                bit.add(posl[v],-1)
            posl[v] = curr_r
        ansl[i] = bit.sum(r)-bit.sum(l-1)

    print('\n'.join(map(str, ansl)))
    # for a in ansl: print(a)
    # print(ql)

if __name__ == "__main__":
    main()