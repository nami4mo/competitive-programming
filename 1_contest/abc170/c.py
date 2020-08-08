x,n = map(int, input().split())
pl = list(map(int, input().split()))

for i in range(0,100):
    if x-i not in pl:
        print(x-i)
        break
    elif x+i not in pl:
        print(x+i)
        break