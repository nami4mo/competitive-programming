k=int(input())

cnt50 = k//50
rem = k%50

al = []
not_num = 50-rem
for i in range(51):
    if i != not_num: al.append(i)

al = [a+cnt50 for a in al]
print(50)
print(*al)