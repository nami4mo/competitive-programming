from math import sqrt
al=[]
for _ in range(int(input())):
    a,b=map(int, input().split())
    if a==b:
        ans=(a-1)*2
        al.append(ans)
        continue

    if a>b:a,b=b,a
    c=a*b
    half=int(sqrt(c))
    half2=(c-1)//half
    ans=(half-1)+(half2-1)
    al.append(ans)
for a in al:print(a)