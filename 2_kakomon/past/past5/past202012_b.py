n=int(input())
s=input()
t=''
for si in s[::-1]:
    if si not in t:t+=si
print(t[::-1])