n=int(input())
t=input()
s='b'
if s==t:
    print(0)
    exit()
for i in range(100):
    if i%3==0:
        s='a'+s+'c'
    elif i%3==1:
        s='c'+s+'a'
    else:
        s='b'+s+'b'
    if s==t:
        print(i+1)
        exit()
print(-1)
