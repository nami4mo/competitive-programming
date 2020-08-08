n = int(input())

n_root = int(n**0.5)
for i in range(n_root,0,-1):
    if n%i == 0:
        a = i
        b = n//i
        print( max( len(str(a)), len(str(b)) )) 
        break