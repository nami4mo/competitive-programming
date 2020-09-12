for _ in range(int(input())):
    r,g,b,w = map(int, input().split())
    n = r+g+b+w
    if n%2 == 0:
        if r%2+g%2+b%2+w%2==0:
            print('Yes')
        else:
            if r*g*b == 0:
                print('No')
            else:
                r-=1
                b-=1
                g-=1
                w+=3
                if r%2+g%2+b%2+w%2==0:
                    print('Yes')
                else:
                    print('No')
    else:
        if r%2+g%2+b%2+w%2==1:
            print('Yes')
        else:
            if r*g*b == 0:
                print('No')
            else:
                r-=1
                b-=1
                g-=1
                w+=3
                if r%2+g%2+b%2+w%2==1:
                    print('Yes')
                else:
                    print('No')