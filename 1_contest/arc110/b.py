n=int(input())
s=input()

if s=='1':
    ans=(10**10)*2
    print(ans)
    exit()
if s=='0':
    print(10**10)
    exit()

# for i in range(n):
#     if     


if s[:2] == '11':
    start = 0
elif s[:2] == '10':
    start = 1
elif s[:2] == '01':
    start = 2
elif s[:2] == '00':
    print(0)
    exit()

ok_fkag = False
for i in range(n):
    if i%3 == 0 and s[i] != '1': 
        break
    if i%3 == 1 and s[i] != '1': 
        break
    if i%3 == 2 and s[i] != '0': 
        break
else:
    ok_fkag = True


for i in range(n):
    if i%3 == 1 and s[i] != '1': 
        break
    if i%3 == 2 and s[i] != '1': 
        break
    if i%3 == 0 and s[i] != '0': 
        break
else:
    ok_fkag = True


for i in range(n):
    if i%3 == 2 and s[i] != '1': 
        break
    if i%3 == 0 and s[i] != '1': 
        break
    if i%3 == 1 and s[i] != '0': 
        break
else:
    ok_fkag = True


if ok_fkag:
    step = 3*10**10 - n - start
    ans = step//3 + 1
    print(ans)
else:
    print(0)