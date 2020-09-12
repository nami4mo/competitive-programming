def ext_gcd(a, b, x, y):
    if b == 0:
        x[0] = 1
        y[0] = 0
        return a
    d = ext_gcd(b, a%b, y, x)
    y[0] -= a//b * x[0]
    return d

# x = [0]
# y = [0]
# ext_gcd(7,4,x,y)
# x,y = x[0],y[0]

n = int(input())
al = list(map(int, input().split()))

if n == 1:
    print(1,1)
    print(al[0]*(-1))
    print(1,1)
    print(0)
    print(1,1)
    print(0)
    exit()

if n == 2:
    print(1,1)
    print(al[0]*(-1))
    print(2,2)
    print(al[1]*(-1))
    print(1,1)
    print(0)
    exit()

if n == 3:
    print(1,1)
    print(al[0]*(-1))
    print(2,2)
    print(al[1]*(-1))
    print(3,3)
    print(al[2]*(-1))
    exit()

rem = n - al[0]
print(1,1)
print(rem)
al[0] = n

x = [0]
y = [0]
ext_gcd(n-1,n,x,y)
x,y = x[0],y[0]

ans2 = []
ans3 = [(-1)*n]
for a in al[1:]:
    v = x*(-1)*a*(n-1)
    ans2.append(v)
    ans3.append((a+v)*(-1))

print(2,n)
print(*ans2)
print(1,n)
print(*ans3)