

# def base_10_to_n(X, n):
#     if (int(X/n)):
#         return base_10_to_n(int(X/n), n)+str(X%n)
#     return str(X%n)



# def main():

#     alp = 'abcdefghijklmnopqrstuvwxyz'
#     n = int(input())

#     s = base_10_to_n(n-1,26)
#     print(s)


# if __name__ == "__main__":
#     main()

alp = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
for i in range(10):
    ind1 = 26*(pow(26,i-1)-1)//25 + 1
    ind2 = 26*(pow(26,i)-1)//25 + 1
    if ind1 <= n < ind2:
        n_len = i

# print(n_len)

n = n
ans = ''
for i in range(20,1,-1):
    curr_a = n%26
    ind = curr_a -1
    if ind == -1: ind = 25
    ans += alp[ind]
    if n < 26:
        break
    n = n//26
    if ind == 25: 
        n=n-1
        if n <= 0:break

print(ans[::-1])