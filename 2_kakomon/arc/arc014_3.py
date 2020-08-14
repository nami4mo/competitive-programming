n = int(input())
s = input()
r = s.count('R')
g = s.count('G')
b = s.count('B')
cnt = r%2 + g%2 + b%2
print(cnt)