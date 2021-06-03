n=int(input())
s=input()
d=['F','D','C','B','A']
for i in range(5):
    s=s.replace(d[i],str(i))
v=0
for si in s:v+=int(si)
print(v/n)
