n,k = map(int, input().split())

ans = 0
abl = []
for _ in range(n):
    a,b = map(int, input().split())
    abl.append((a,b))

max_bit = 0
for i in range(31):
    if k < pow(2,i):
        max_bit = i
        break

k_bits = [-1]*(max_bit)
for i in range(max_bit-1,-1,-1):
    if k&(1<<i) > 0:
        k_bits[i] = 1
    else:
        k_bits[i] = 0

# print(k_bits)

k_bits = k_bits[::-1]
bits_cands = []
bits_cands.append(k_bits[::-1])
for i in range(max_bit):
    curr_row = []
    for j in range(0,i):
        curr_row.append(k_bits[j])
    if k_bits[i] == 1:
        curr_row.append(0)
        curr_row = curr_row + [1]*(max_bit-1-i)
    else:
        for j in range(i,max_bit):
            curr_row.append(k_bits[j])
    bits_cands.append(curr_row[::-1])

# print(bits_cands)
ans = 0
for bits in bits_cands:
    val = 0
    for a,b in abl:
        if a > k: continue
        for i in range(max_bit):
            if a&(1<<i) > 0 and bits[i] == 0:
                break
        else:
            val += b
    ans = max(ans,val)
print(ans)

# bits_cands = []
# print(max_bit)
# curr = [1]
# for i in range(max_bit-1,-1,-1):
#     if k%(1<<i) == 0:
#         curr.append(0)
#         row = curr + []