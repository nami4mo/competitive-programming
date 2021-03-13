a,b,w=map(int, input().split())
w*=1000

mins=(w-1)//b+1
maxs=w//a

if mins>maxs:
    print('UNSATISFIABLE')
else:
    print(mins,maxs)
