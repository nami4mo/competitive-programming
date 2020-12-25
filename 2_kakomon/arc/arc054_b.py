def y(x,p):
    return x+p*pow(2,-x/1.5)

p=float(input())
left = 0
right = 100
while abs(left-right)>10**(-12):
    d = (right-left)/3
    c1 = left+d
    c2 = right-d
    if y(c1,p) > y(c2,p):
        left = c1
    else:
        right = c2

print(y(left,p))