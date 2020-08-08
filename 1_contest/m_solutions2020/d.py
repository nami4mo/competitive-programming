
# 13
# 5 5 6 7 6 6 5 6 7 7 7 6 6 7

def main():
    n = int(input())
    al = list(map(int, input().split()))
    
    buy_is = []
    sell_is = []

    if n == 2:
        if al[0] < al[1]:
            money = 1000
            buy_kabu = 1000//al[0]
            money -= (buy_kabu*al[0])
            money += al[1]*buy_kabu
            print(money)
        else:
            print(1000)
        exit()


    if al[0] < al[1]:
        buy_is.append(0)

    
    for i, (a0,a1,a2) in enumerate( zip(al[0:-2], al[1:-1], al[2:]) ):
        if a0 >= a1 and a1 < a2:
            buy_is.append(i+1)
        elif a0 <= a1 and a1 > a2:
            sell_is.append(i+1)


    money = 1000
    kabu = 0
    for i in range(n):
        if i in buy_is:
            buy_kabu = money//al[i]
            kabu += buy_kabu
            money -= (buy_kabu*al[i])
        elif i in sell_is or i == n-1:
            money += al[i]*kabu
            kabu = 0
    
    print(money)
    # print(buy_is)
    # print(sell_is)

if __name__ == "__main__":
    main()