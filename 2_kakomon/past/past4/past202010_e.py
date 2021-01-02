from itertools import permutations

n = int(input())
s = input()

ll = list(range(0,n))  # list of elements
perml = list(permutations(ll, n))

for perm in perml:
    new_s = ''
    for p in perm:
        new_s += s[p]
    if s != new_s[::-1] and s != new_s:
        print(new_s)
        exit()
print('None')
