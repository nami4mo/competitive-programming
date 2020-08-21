n = int(input())  
start = int(n**0.5)

for i in range(start,0,-1):
    if n%i == 0:
        s = str(n//i)
        keta = len(s)
        print(keta)
        break
