y,m,d=map(int,input().split('/'))
e30=[4,6,9,11]
while True:
    if y%m==0 and (y//m)%d==0:
        print(f'{y}/{m:02}/{d:02}')
        exit()
    if d==28 and y%4!=0 and m==2:
        d,m=1,m+1
    elif d==28 and m==2 and y%100==0 and y%400!=0:
        d,m=1,m+1
    elif d==29 and y%4==0 and m==2:
        d,m=1,m+1
    elif d==30 and m in e30:
        d,m=1,m+1
    elif d==31:
        d,m=1,m+1
    else:
        d+=1
    
    if m==13:
        print(f'{y+1}/01/01')
        exit()
