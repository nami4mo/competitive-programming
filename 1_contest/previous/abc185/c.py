l=int(input())

ans=1
cl = l-1
cr = 11

for i in range(cr):
    ans *= (cl-i)

for i in range(cr):
    ans //= (i+1)

print(ans)