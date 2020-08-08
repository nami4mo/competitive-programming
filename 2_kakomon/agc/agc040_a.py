
import math

def main():
    s = str(input())
    first = s[0]
    cnt_l = []
    tmp_cnt = 1
    prev_s = first
    for curr_s in s[1:]:
        if prev_s != curr_s:
            cnt_l.append(tmp_cnt)
            tmp_cnt = 1
        else:
            tmp_cnt+=1
        prev_s = curr_s
    cnt_l.append(tmp_cnt)

    ans_l = []
    last_num = 0
    if first == '>':
        down_cnt = cnt_l[0]
        for d in range(down_cnt):
            ans_l.append(down_cnt-d)
        cnt_l = cnt_l[1:]

    # if first == '<':
    # print(cnt_l)
    ans_l.append(0)
    last_num = 0
    for i in range(math.ceil(len(cnt_l)/2)):
        # print('i',i)
        up_cnt = cnt_l[i*2]
        if i*2+1 >= len(cnt_l):
            down_cnt = 0
        else:
            down_cnt = cnt_l[i*2+1]
        # print(up_cnt,down_cnt)
        # print()
        for u in range(up_cnt):
            if u != up_cnt-1:
                last_num+=1
                ans_l.append(last_num)
            else:
                last_num = max(last_num+1, down_cnt)
                ans_l.append(last_num)
        for d in range(down_cnt):
            if d==0:
                if last_num > down_cnt:
                    last_num = down_cnt-1
                else:
                    last_num-=1
                ans_l.append(last_num)
            else:
                last_num-=1
                ans_l.append(last_num)

    # print(ans_l)
    print(sum(ans_l))

if __name__ == "__main__":
    main()