

def main():
    n = int(input())
    rl = list(map(int, input().split()))
    diffl = []
    for r0,r1 in zip(rl[:-1], rl[1:]):
        d = r1-r0
        if d != 0:
            diffl.append(d)

    ans = 0
    for d0,d1 in zip(diffl[:-1], diffl[1:]):
        if d0*d1 < 0:
            ans += 1
    
    if ans > 0:
        print(ans+2)
    else:
        print(0)

if __name__ == "__main__":
    main()