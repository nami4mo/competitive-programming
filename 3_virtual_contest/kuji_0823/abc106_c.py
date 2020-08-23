s = input()
k = int(input())    



for si in s[:k]:
    sii  = int(si)
    if sii != 1:
        print(sii)
        exit()
else:
    print(1)