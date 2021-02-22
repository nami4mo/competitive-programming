# n,m=map(int, input().split())
# al=[]
# for _ in range(n):
#     row=list(map(int, input().split()))
#     al.append(row)

k4=set()
for i in range(100):
    k4.add(i**4)
    k4.add(-(i**4))
for i in range(3,30):
    for j in range(15,10**6,15):
        if j-i in k4:
            print(i,j)