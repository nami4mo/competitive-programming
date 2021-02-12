cnts = [1]
curr_2_sum = 1
csum = 1
for i in range(1,50):
    curr_2_sum += 2**i
    v = (1+curr_2_sum)*curr_2_sum//2
    # print(v)
    # cnts.append(v)
    csum += v
    if csum > 10**18: break
    else: cnts.append(csum)

# print(cnts)
# print(len(cnts))
ansl = []
for _ in range(int(input())):
    n=int(input())
    for i in range(30):
        if cnts[i] > n:
            ansl.append(i)
            break
    else:
        ansl.append(30)

for ans in ansl: print(ans)