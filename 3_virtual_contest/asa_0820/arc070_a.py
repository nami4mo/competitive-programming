x = int(input())

for i in range(1,10**5):
    curr_max = i*(i+1)//2
    if curr_max >= x:
        print(i)
        break