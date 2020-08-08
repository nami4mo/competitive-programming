import heapq
import sys
input = sys.stdin.readline

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
                # self.d.pop(self.h[0])
                heapq.heappop(self.h)
            else:
                break


    def get_min(self):
        return self.h[0]


    def pop(self):
        poped_val = self.h[0]
        self.erase(poped_val)
        return poped_val


    def exist(self, x):
        return (x in self.d and self.d[x] > 0)


    def show_h(self):
        print(self.h)
        elems = [v for v in self.h if self.d[v] > 0]
        print(elems)


    def show_d(self):
        print(self.d)



def main():
    hd = HeapDict()
    hd.insert(6)
    hd.insert(5)
    hd.insert(4)
    hd.insert(3)
    hd.insert(2)
    hd.insert(1)
    hd.insert(3)
    hd.insert(3)
    hd.insert(3)
    hd.show_h()
    hd.erase(4)
    while hd.h:
        print(hd.pop())



if __name__ == "__main__":
    main()