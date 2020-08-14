n = int(input())
al = list(map(int, input().split()))
boxs = []
cnts = [0]*(n+1)


for i in range(n,0,-1):
    if cnts[i]%2 != al[i-1]:
        boxs.append(i)
        for j in range(1, int(i**0.5)+1):
            if i%j == 0:
                cnts[j] += 1
                if j*j != i: cnts[i//j] += 1


print(len(boxs))
for b in boxs: print(b)