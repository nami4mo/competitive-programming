d=set()
for i in range(int(input())):
    s=input()
    if s in d:continue
    print(i+1)
    d.add(s)