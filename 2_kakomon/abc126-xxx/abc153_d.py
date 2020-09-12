
h = int(input())

# curr_n = 0
curr_2_njou = 1
while True:
    if h < curr_2_njou:
        break
    else:
        curr_2_njou*=2

print(curr_2_njou-1)