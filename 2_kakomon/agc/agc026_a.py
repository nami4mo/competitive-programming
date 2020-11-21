n = int(input())
al = list(map(int, input().split()))

# if n == 0:
#     ans1 = 0
#     for i in range(n):
#         if i%2 == 0 and al[i] == 1:
#             ans1+=1
#         elif i%2 == 1 and al[i] == 2:
#             ans1+=1
#     ans2 = 0
#     for i in range(n):
#         if i%2 == 0 and al[i] == 2:
#             ans2+=1
#         elif i%2 == 1 and al[i] == 1:
#             ans2+=1
#     print(min(ans1,ans2))

# else:
ans = 0
prev = -1
for i in range(n):
    if prev == al[i]:
        ans += 1
        prev = -1
    else:
        prev = al[i]
print(ans)