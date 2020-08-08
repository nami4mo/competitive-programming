# ------- HeapDict ----------
import heapq
from collections import deque
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
        if not self.h:
            return None
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



def main():

    n,x = map(int, input().split())
    tl = list(map(int, input().split()))
    al = list(map(int, input().split()))

    if sum(al) < x:
        print(-1)
        exit()

    ng, ok = 0,10**5+2
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        hd = HeapDict()
        tal = [ [] for _ in range(10**5+2)]
        for t,a in zip(tl,al):
            tal[t].append(a)
        
        for t in range(10**5,mid,-1):
            for v in tal[t]:
                hd.insert(v*(-1))
        
        curr_val = 0
        ok_flag = False
        for t in range(mid, 0, -1):
            for v in tal[t]:
                hd.insert(v*(-1))
            poped = hd.pop()
            if poped:
                curr_val += (-1)*poped
            if curr_val >= x:
                ok_flag = True
                break

        if ok_flag:
            ok = mid
        else:
            ng = mid
    if ok == 10**5+2: ok = -1
    print(ok)




if __name__ == "__main__":
    main()