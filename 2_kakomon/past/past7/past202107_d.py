n=int(input())
s=input()
for ss in ['a','i','u','e','o']:
    sss=ss+'x'+ss
    s=s.replace(sss,'...')
print(s)