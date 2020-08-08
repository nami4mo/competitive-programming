from collections import deque

def main():
    n = int(input())
    nums = []
    for i in range(2,n+1):
        nums.append((i,i,{}))

    deq = deque(nums)
    while deq:
        curr_num, orig_num, comb = deq.popleft()
        comb_num = 1
        comb.setdefault(curr_num,0)
        comb[curr_num] += 1
        for v in comb.values():
            comb_num *= (comb_num+1)
        ans += orig_num+comb_num



if __name__ == "__main__":
    main()