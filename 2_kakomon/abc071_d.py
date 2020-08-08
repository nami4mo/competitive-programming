n = int(input())
s1 = list(input())
s2 = list(input())

MOD = 10**9+7
i = 0
ans = 0
prev_double = True

if s1[0] == s2[0]:
    prev_double = False
    i = 1
    ans = 3
else:
    prev_double = True
    i = 2
    ans = 6

while i < n:
    if s1[i] == s2[i]:
        i += 1
        if prev_double:
            ans *= 1
        else:
            ans *= 2
        prev_double = False
    else:
        i+=2
        if prev_double:
            ans *= 3
        else:
            ans *= 2
        prev_double = True
    ans %= MOD
print(ans)