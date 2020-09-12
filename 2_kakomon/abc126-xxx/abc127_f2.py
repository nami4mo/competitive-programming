from heapq import heappop, heappush
class MedianContainer:
    def __init__(self):
        self._left_q = []
        self._right_q = []
        self._left_sum = 0
        self._right_sum = 0
        self._med1, self._med2 = None, None
        self._med = None

    def insert(self, x):
        if not any([self._med, self._med1, self._med2]): # First insert
            self._med = x
        elif self._med is None and self._med1 is not None and self._med2 is not None:
            if x <= self._med1:
                heappush(self._left_q, x*(-1))
                heappush(self._right_q, self._med2)
                self._left_sum += x
                self._right_sum += self._med2
                self._med = self._med1
            elif x >= self._med2:
                heappush(self._left_q, self._med1*(-1))
                heappush(self._right_q, x)
                self._left_sum += self._med1
                self._right_sum += x
                self._med = self._med2
            else:
                heappush(self._left_q, self._med1*(-1))
                heappush(self._right_q, self._med2)
                self._left_sum += self._med1
                self._right_sum += self._med2
                self._med = x
            self._med1, self._med2 = None, None
        else:
            if x <= self._med:
                heappush(self._left_q, x*(-1))
                self._med1 = heappop(self._left_q)*(-1)
                self._left_sum += x
                self._left_sum -= self._med1
                self._med2 = self._med
            else:
                heappush(self._right_q, x)
                self._right_sum += x
                self._med1 = self._med
                self._med2 = heappop(self._right_q)
                self._right_sum -= self._med2
            self._med = None

        
    def get_med(self):
        if self._med is not None:
            return [self._med]
        else:
            return [self._med1, self._med2]


    def get_left_sum(self):
        return self._left_sum


    def get_right_sum(self):
        return self._right_sum


    def get_half_len(self):
        return len(self._left_q)

q = int(input())
const_b = 0
ansl = []

mc = MedianContainer()
for _ in range(q):
    row = list(input().split())
    if row[0] == '2':
        half_len = mc.get_half_len()
        meds = mc.get_med()
        if len(meds) == 1:
            left_sum = meds[0]*half_len - mc.get_left_sum()
            right_sum = mc.get_right_sum() - meds[0]*half_len
            ans = left_sum + right_sum + const_b
            ansl.append((meds[0],ans))
        else:
            left_sum = meds[0]*half_len - mc.get_left_sum()
            right_sum = mc.get_right_sum() - meds[0]*half_len
            ans = left_sum + right_sum + (meds[1]-meds[0]) + const_b
            ansl.append((meds[0],ans))
    
    else:
        a,b = int(row[1]), int(row[2])
        const_b += b
        mc.insert(a)


for ax,av in ansl:
    print(ax,av)