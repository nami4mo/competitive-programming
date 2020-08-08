
def main():
    n, a, b = map(int, input().split()) 

    ab_diff = abs(a-b)
    if ab_diff%2 == 0:
        print(ab_diff//2)
        return
    
    a_edge_diff = min(abs(a-1),abs(n-a))
    b_edge_diff = min(abs(b-1),abs(n-b))
    # near_diff = min(a_edge_diff, b_edge_diff)
    if a_edge_diff <= b_edge_diff:
        print(a_edge_diff+1+ (ab_diff-1)//2)
    else:
        print(b_edge_diff+1+ (ab_diff-1)//2)

if __name__ == "__main__":
    main()