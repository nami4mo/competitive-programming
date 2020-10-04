n = int(input())
al = list(map(int, input().split()))
exist = [False]*(10**5+1)

r = 0
ans = 0
for l in range(n):
    while r < n:
        if not exist[al[r]]:
            exist[al[r]] = True
            r += 1
        else:
            break
    ans = max(ans,r-l)
    exist[al[l]] = False

print(ans)
    


# l = 0
# r = 0
# # el[] = True
# ans = 0
# while r < n:
#     if el[al[r]] == False:
#         el[al[r]] = True
#         r += 1
#         ans = max(ans,r-l)
#     else:
#         poped = al[r]
#         while True:
#             el[al[l]] = False
#             l += 1
#             if al[l-1] == poped:
#                 break

# print(ans)