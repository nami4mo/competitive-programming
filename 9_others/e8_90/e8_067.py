def b8_b10(s):
    return int(s, 8)

def b10_b9(b10):
    v=[]
    while b10>0:
        v.append(str(b10%9))
        b10//=9
    if not v: v=['0']
    v=v[::-1]
    v=''.join(v)
    return v

def b9_b10(s):
    return int(s, 9)
    

n,k=map(int, input().split())

b8=str(n)
for _ in range(k):
    b10n=b8_b10(b8)
    b9=b10_b9(b10n)
    b8=b9.replace('8','5')

print(b8)
