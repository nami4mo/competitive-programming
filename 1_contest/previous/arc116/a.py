
ansl=[]
for _ in range(int(input())):
    n=int(input())
    if n%4==0:
        ansl.append('Even')
    elif n%2==0:
        ansl.append('Same')
    else:
        ansl.append('Odd')
for a in ansl:print(a)