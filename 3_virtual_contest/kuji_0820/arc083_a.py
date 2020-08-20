from bisect import bisect_left, bisect_right

a,b,c,d,e,f= map(int, input().split())
a *= 100
b *= 100

ws = set()
for i in range(31):
    for j in range(31):
        v = a*i + b*j
        if 0 < v <= f:
            ws.add(v) 
waters = list(ws)
waters.sort()

ss = set()
for i in range(3001):
    for j in range(3001):
        v = i*c +j*d
        if v <= f:
            ss.add(v)
        else:
            break 

sugars = list(ss)
sugars.sort()

max_sugar, max_water = 0, waters[0]
for w in waters:
    s_max1 = f - w
    s_max2 = (w//100)*e
    s_max = min(s_max1, s_max2)
    ind = bisect_right(sugars, s_max) - 1
    ind = ind if 0 <= ind < len(sugars) else None
    if ind is None:
        continue
    else:
        sugar = sugars[ind] if ind is not None else None
        if sugar*(max_sugar+max_water) > max_sugar*(sugar+w):
            max_sugar = sugar
            max_water = w

print(max_sugar+max_water, max_sugar)
