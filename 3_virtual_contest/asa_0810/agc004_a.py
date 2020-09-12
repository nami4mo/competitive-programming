a,b,c = map(int, input().split())

if a%2 == 0 or b%2 == 0 or c%2 == 0:
    print(0)
    exit()

al = [a,b,c]
al.sort()
print(al[0]*al[1])