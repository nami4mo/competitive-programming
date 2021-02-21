n=int(input())
sl=[list(input()) for _ in range(n)]
tl=[list(input()) for _ in range(n)]

ans1=0
for i in range(n):
    for j in range(n):
        if sl[i][j]!=tl[i][j]:ans1+=1

ans2=0
for i in range(n):
    for j in range(n):
        if sl[i][j]!=tl[j][n-1-i]:ans2+=1

ans3=0
for i in range(n):
    for j in range(n):
        if sl[i][j]!=tl[n-1-j][i]:ans3+=1

ans4=0
for i in range(n):
    for j in range(n):
        if sl[i][j]!=tl[n-1-i][n-1-j]:ans4+=1

# print(ans1,ans2,ans3)
print(min(ans1,ans2+1,ans3+1,ans4+2))