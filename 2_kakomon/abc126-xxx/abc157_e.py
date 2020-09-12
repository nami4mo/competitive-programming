import heapq
class HeapDict:
    def __init__(self):
        self.h = []
        self.d = {}

    def insert(self,x):
        if x not in self.d or self.d[x] == 0:
            heapq.heappush(self.h, x)
        self.d.setdefault(x,0)
        self.d[x] += 1


    def erase(self,x):
        if x not in self.d or self.d[x] == 0:
            return
        else:
            self.d[x] -= 1

        while self.h:
            if self.d[self.h[0]] == 0:
                heapq.heappop(self.h)
            else:
                break


    def get_min(self):
        if not self.h:
            return None
        else:
            return self.h[0]


    def pop(self):
        poped_val = self.h[0]
        self.erase(poped_val)
        return poped_val


    def exist(self, x):
        return (x in self.d and self.d[x] > 0)


    def show_h(self):
        elems = [v for v in self.h if self.d[v] > 0]
        print(elems)


    def show_d(self):
        print(self.d)

alps = 'abcdefghijklmnopqrstuvwxyz'

n = int(input())
s = input()
char_hd_d = {}
for alp in alps:
    char_hd_d[alp] = HeapDict()

for i, si in enumerate(s):
    char_hd_d[si].insert(i+1)

q = int(input())
ansl = []
for _ in range(q):
    command, a, b = input().split()
    if command == '1':
        i = int(a)
        c = b
        i_char = s[i-1]
        char_hd_d[i_char].erase(i)
        char_hd_d[c].insert(i)
    else:
        l,r = int(a),int(b)
        l_cnt = 0
        r_cnt = 0
        for alp in alps:
            alp_min = char_hd_d[alp].get_min()
            if alp_min is not None:
                if alp_min <= r:
                    r_cnt += 1
                if alp_min <= l-1:
                    l_cnt += 1
        ans = r_cnt-l_cnt
        ansl.append(ans)
        print('-------')
        print(ans, flush=True)
        print(l_cnt,r_cnt)

for a in ansl:
    print(a)            