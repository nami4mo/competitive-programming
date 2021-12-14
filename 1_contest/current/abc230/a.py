n=int(input())
if n<42:
    s=str(n).zfill(3)
    print('AGC'+s)
else:
    s=str(n+1).zfill(3)
    print('AGC'+s)