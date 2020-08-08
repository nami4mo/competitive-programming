s = input()
t = input()

ams = 0
for i in range(len(s)):
    if s[i] != t[i]: ams += 1

print(ams)