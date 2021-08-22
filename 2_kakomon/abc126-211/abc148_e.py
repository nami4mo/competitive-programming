
def main():
    n = int(input())
    if n%2 == 1:
        print(0)
        return
    
    five_cnt = 0
    for i in range(1,25+1):
        base = 2*(5**i)
        five_cnt += n//base

    print(five_cnt)

if __name__ == "__main__":
    main()