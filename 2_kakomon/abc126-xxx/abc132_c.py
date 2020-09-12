n = int(input())
dl = list(map(int, input().split()))

dl.sort()
d_half1 = dl[n//2-1]
d_half2 = dl[n//2]

print(d_half2-d_half1)