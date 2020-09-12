def main():
    n, k = map(int, input().split()) 
    al = list(map(int, input().split())) 
    city_l = [1]
    city_s = set([1])
    loop_city_l = []
    curr_city = 1
    cnt = 0
    for i in range(1,k+1):
        next_c = al[curr_city-1]
        if next_c in city_s:
            cnt = i
            first_city = city_l.index(next_c)
            loop_city_l = city_l[first_city:]
            break
        else:
            city_s.add(next_c)
            city_l.append(next_c)
        curr_city = next_c
    else:
        print(curr_city)
        return

    # print(loop_city_l)
    remained = k-cnt
    last_pos = remained%len(loop_city_l)
    print(loop_city_l[last_pos])

if __name__ == "__main__":
    main()

