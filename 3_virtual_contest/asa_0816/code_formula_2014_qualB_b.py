n = input()
n = n[::-1]
odd = 0
even = 0
for i, ni in enumerate(n):
    if (i+1)%2 == 0:
        odd += int(ni)
    else:
        even += int(ni)     

print(odd,even)