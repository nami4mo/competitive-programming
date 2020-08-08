n = int(input())
al = list(map(int, input().split())) 
al = set(al)
if len(al)%2 == 0:
    print(len(al)-1)
else:
    print(len(al))
