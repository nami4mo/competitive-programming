n = int(input())
a = n//3600
rem = n - a*3600
b = rem//60
c = n%60
a = str(a).zfill(2)
b = str(b).zfill(2)
c = str(c).zfill(2)
ans = a+':'+b+':'+c
print(ans)