el = list(map(int, input().split()))
b = int(input())
ll = list(map(int, input().split()))

cnt = 0
bonus = False
for l in ll:
    if l in el: cnt += 1
    elif l == b: bonus = True

if cnt == 6: print(1)
elif cnt == 5 and bonus: print(2)
elif cnt == 5: print(3)
elif cnt == 4: print(4) 
elif cnt == 3: print(5)
else: print(0)

