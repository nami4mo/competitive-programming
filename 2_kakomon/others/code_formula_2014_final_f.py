al=[]
row=[]
csum=0
for i in range(100,0,-1):
    if csum+i<=650:
        row.append(i)
        csum+=i
    else:
        crow=row[:]
        al.append(crow)
        row=[i]
        csum=0
al.append(row)
# print(al)
x=100
ansl=[]
for row in al:
    # x+=row[0]*2
    y=row[0]
    for r in row:
        # print(x,y)
        ansl.append((x,y))
        y+=r*2
    x+=row[0]*2

# i=1
for x,y in ansl[::-1]:
    print(x,y)
    # i+=1