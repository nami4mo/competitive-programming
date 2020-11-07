n = int(input())
al = list(map(int, input().split()))

a1 = 0
a2 = 0
a3 = 0
for a in al:
    a1 += abs(a)
    a2 += a*a
    a3 = max(a3, abs(a))

print(a1)
print(a2**0.5)
print(a3)