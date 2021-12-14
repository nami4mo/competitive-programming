a,b=map(int, input().split())
a=str(a).zfill(20)
b=str(b).zfill(20)
for i in range(20):
    if int(a[i])+int(b[i])>=10:
        print('Hard')
        exit()
print('Easy')