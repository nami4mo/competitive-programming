s = input()

for i in range(10):
    if str(i)*2 in s:
        print('Bad')
        exit()
print('Good')