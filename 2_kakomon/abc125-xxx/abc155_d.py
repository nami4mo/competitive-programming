from bisect import bisect_left, bisect_right
from math import ceil

def main():
    n,k = map(int, input().split())
    al = list(map(int, input().split()))
    al.sort()

    al_n = []
    al_p = []
    al_n_p = []
    zero_cnt = 0
    for a in al:
        if a < 0: 
            al_n.append(a)
            al_n_p.append(-1*a)
        elif a > 0: 
            al_p.append(a)
        else: 
            zero_cnt += 1
    al_n_p = al_n_p[::-1]

    n_cnt = len(al_n)
    p_cnt = len(al_p)

    m_n_cnt = n_cnt*p_cnt
    m_p_cnt = n_cnt*(n_cnt-1)//2 + p_cnt*(p_cnt-1)//2
    m_zero_cnt = zero_cnt*(n_cnt+p_cnt) + zero_cnt*(zero_cnt-1)//2


    if k <= m_n_cnt:
        left = (-1)*(10**18)
        right = -1
        while right-left>1:
            curr_num = left + (right-left)//2
            curr_cnt = 0
            num_exist = False
            for an in al_n:
                targt_p = abs(curr_num)//abs(an)
                p_ind = bisect_right(al_p,targt_p)
                ok_p_cnt = len(al_p) - p_ind
                curr_cnt += ok_p_cnt
                if p_ind > 0 and al_p[p_ind-1]*an == curr_num:
                    num_exist = True
            
            if curr_cnt > k-1:
                right = curr_num
            elif curr_cnt < k-1:
                left = curr_num
            else:
                if num_exist:
                    print(curr_num)
                    exit()
                else:
                    left = curr_num


    elif m_n_cnt < k <= m_n_cnt+m_zero_cnt:
        print(0)
        exit()

    else:
        k = k - m_n_cnt - m_zero_cnt # 1-index
        right = (10**18)
        left = 0
        while right-left > 1:
            cnt = k
            # print(f'k:{k}')
            # print('----')
            curr_num = left + (right-left)//2
            curr_cnt = 0
            num_exist = False
            # curr_num = 6
            # print(curr_num, left, right)
            for i, an in enumerate(al_n_p):
                targt_p = abs(curr_num)//abs(an)
                ok_p_cnt = max(bisect_right(al_n_p,targt_p)-i-1, 0)
                cnt -= ok_p_cnt
            
            for i, an in enumerate(al_p):
                # print(f'----- {an} -----')
                targt_p = abs(curr_num)//abs(an)
                
                ok_p_cnt = max(bisect_right(al_p,targt_p)-i-1, 0)
                cnt -= ok_p_cnt
                # print(ok_p_cnt)

            if cnt > 0:
                left = curr_num
            else:
                right = curr_num

        print(right)


if __name__ == "__main__":
    main()