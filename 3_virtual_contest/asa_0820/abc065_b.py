n = int(input())
al = [0]*(n+1)
for i in range(n):
    al[i+1] = int(input())
    
curr = 1
for i in range(10**5+1):
    next_pos = al[curr]
    if next_pos == 2:
        print(i+1)
        break
    else:
        curr = next_pos
else:
    print(-1)