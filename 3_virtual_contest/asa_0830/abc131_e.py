n,k = map(int, input().split())
# cnt = 0
# rem = 0
# for i in range(25):
#     if i*(i-1)//2 >= k:
#         cnt = i+1
#         rem = i*(i-1)//2 - k
#         break

ansl = []
for i in range(n-1):
    ansl.append((1,i+2))

com = (n-1)*(n-2)//2
rem = com - k
if rem < 0:
    print(-1)
    exit()

cu = 2
cv = 3
for i in range(rem):
    if cv > n:
        cu += 1
        cv = cu+1
    ansl.append((cu,cv))
    cv += 1

print(len(ansl))
for u,v in ansl:
    print(u,v)

# print(cnt)
# print(rem)