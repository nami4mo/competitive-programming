x = int(input())
bekis = [1]
for i in range(2,35):
    for j in range(2,15):
        v = i**j
        if v > x: break
        bekis.append(v)

bekis.sort()
print(bekis[-1])