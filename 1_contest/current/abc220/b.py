k=int(input())
a,b=map(str, input().split())
a=a[::-1]
b=b[::-1]

aa=0
bb=0
for i in range(len(a)):
    aa+=int(a[i])*pow(k,i)

for i in range(len(b)):
    bb+=int(b[i])*pow(k,i)
print(aa*bb)