from itertools import product

h,w = 2,3
ite_h = product(range(2),repeat=h)
ite_w = product(range(2),repeat=w)
print(ite_h)
# ite_h = list(ite_h)
# ite_w = list(ite_w)

for bit_h in ite_h:
    for bit_w in ite_w:
        print(bit_h, bit_w)