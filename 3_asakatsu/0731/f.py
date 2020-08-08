from collections import deque

# ------- HeapDict ----------
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



def main():
    n,k = map(int, input().split())
    pl = list(map(int, input().split()))
    pmin = -1
    pmax = n
    hd_min = HeapDict()
    hd_max = HeapDict()
    q = deque(pl[:k])
    # pmin = min(pl[:k])
    # pmax = max(pl[:k])
    ans = 1
    last_change = -1
    pk_sort = sorted(pl[:k])
    for i in range(k-1,-1,0):
        if pk_sort[i] != pl[i]:
            last_change = i
            break

    for p in pl[:k]:
        hd_min.insert(p)
        hd_max.insert(-1*p)

    for i in range(k,n):
        in_val = pl[i]
        out_val = q[0]
        q_min = hd_min.get_min()
        q_max = hd_max.get_min() * (-1)
        if (in_val < q_max or out_val > q_min) and last_change < i-k:
            ans += 1
        hd_min.erase(out_val)
        hd_max.erase(out_val*(-1))
        hd_min.insert(in_val)
        hd_max.insert(in_val*(-1))
        q.popleft()
        q.append(in_val)

    print(ans)

if __name__ == "__main__":
    main()