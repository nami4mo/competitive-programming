
def main():
    x = int(input())

    # i = 0
    # while True:
    #     if (i+1)**5 - i**5 > 10**9:
    #         break
    #     i+=1
    # print(i)

    for a in range(-119,120):
        for b in range(-119, 120):
            if a**5-b**5 == x:
                print(a, b)
                return

if __name__ == "__main__":
    main()