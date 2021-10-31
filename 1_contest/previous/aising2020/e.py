

def main():
    t = int(input())
    ansl = []
    for _ in range(t):
        n = int(input())
        ls = []
        rs = []
        for n_ in range(n):
            k,l,r = map(int, input().split())
            if l-r >= 0:
                ls.append((k,l,r))
            else:
                rs.append((k,l,r))
            ls.sort()
            rs.sort(reverse=True) 
            for k,l,r in ls:
                   


if __name__ == "__main__":
    main()