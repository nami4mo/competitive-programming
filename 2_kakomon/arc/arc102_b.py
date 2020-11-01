l = int(input())
min2 = 0
for i in range(21):
    if pow(2,i) > l:
        min2 = i-1
        break

# print(min2)
ansl = []
for i in range(min2):
    u = i+1
    v = i+2
    w1 = 0
    w2 = pow(2,i)
    ansl.append((u,v,w1))
    ansl.append((u,v,w2))

rem = l - pow(2,min2)
bin_str = bin(rem)
bin_sr = bin_str[::-1]
n = min2+1
prev_plus = pow(2,min2)
for i,b in enumerate(bin_sr):
    if b == '1':
        ansl.append((i+1,n,prev_plus))
        prev_plus += pow(2,i)

print(min2+1,len(ansl))
for a in ansl: print(*a)