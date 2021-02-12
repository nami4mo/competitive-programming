def main():
    n_ansl = [0]*(2*(10**5))
    for i in range(1,2*(10**5)):
    # for i in range(1,20):
        cnt = 0
        one_cnt = bin(i).count("1")
        rem = i
        while rem != 0:
            one_cnt = bin(rem).count("1")
            rem = rem%one_cnt   
            cnt += 1
        n_ansl[i] = cnt
 
    n = int(input())
    x = list(input())
    one_cnt = x.count('1')

    if one_cnt == 0:
        for i in range(n):
            print(1)
        exit()
    
    x = x[::-1]

    curr_sum_p1 = 0
    curr_sum_m1 = 0
    dummy = 1
    for i, xi in enumerate(x):
        if xi == '1':
            curr_sum_p1 += pow(2,i,one_cnt+1)
            curr_sum_p1%=(one_cnt+1)
            if one_cnt > 1:
                curr_sum_m1 += pow(2,i,one_cnt-1)
                curr_sum_m1%=(one_cnt-1)
        dummy *= 2
        dummy %= (one_cnt+1)
        
    ansl = [0]*(n)
    for i, xi in enumerate(x):
        if xi == '1':
            if one_cnt > 1:
                diff = (-1)*pow(2,i,one_cnt-1)
                ans = (curr_sum_m1 + diff)%(one_cnt-1)
                ansl[i] = n_ansl[ans]+1
            else:
                ansl[i] = 0
        else:
            diff = pow(2,i,one_cnt+1)
            ans = (curr_sum_p1 + diff)%(one_cnt+1)
            ansl[i] = (n_ansl[ans]+1)
 
 
    # print(ansl)
    for a in ansl[::-1]:
        print(a)
 
if __name__ == "__main__":
    main()