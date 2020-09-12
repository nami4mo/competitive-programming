d = int(input())
cl = list(map(int, input().split()))
sl = []
for _ in range(d):
    sl.append(list(map(int, input().split())))

for i in range(d):
    print(i%26 + 1)